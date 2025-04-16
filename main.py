import asyncio
import logging
import sys
import os
from datetime import datetime, timedelta
from typing import Dict, List, Tuple, Any

import pytz
from timezonefinder import TimezoneFinder

from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters.command import Command
from aiogram.types import Message, CallbackQuery, FSInputFile, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from settings import settings
from db import db
from repository.user import UserRepository
from repository.events import EventsRepository
from repository.reminders import RemindersRepository
from repository.books import BooksRepository
from keyboards import create_events_keyboard, create_event_details_keyboard, create_books_keyboard, create_book_details_keyboard, create_instance_selection_keyboard


def get_event_timezone(event: Dict[str, Any]) -> pytz.timezone:
    """Get timezone for an event from event data"""
    try:
        if event.get('timezone'):
            return pytz.timezone(event['timezone'])
    except Exception as e:
        logging.error(f"Error getting timezone from event data: {e}")
    
    # Fallback to Helsinki timezone if timezone data is not available
    return pytz.timezone('Europe/Helsinki')

def format_event_time(event: Dict[str, Any]) -> str:
    """Format event time with timezone information"""
    try:
        # Get the event's timezone
        event_tz = get_event_timezone(event)
        
        # Ensure the input time is timezone-aware (UTC)
        if event['start_time'].tzinfo is None:
            utc_time = pytz.UTC.localize(event['start_time'])
        else:
            utc_time = event['start_time']
        
        # Convert to event's local time
        local_time = utc_time.astimezone(event_tz)
        
        return f"{local_time.strftime('%d %b %Y, %H:%M')}"
    except Exception as e:
        logging.error(f"Error formatting event time: {e}")
        # Fallback to simple formatting if there's an error
        return event['start_time'].strftime('%d %b %Y, %H:%M')

# Initialize repositories
user_repo = UserRepository()
events_repo = EventsRepository(api_key=settings.LUMA_API_KEY)
reminders_repo = RemindersRepository()
books_repo = BooksRepository()

# Initialize storage
storage = MemoryStorage()

# Initialize dispatcher
dp = Dispatcher(storage=storage)

current_events: Dict[str, Dict] = {}
EVENTS_CACHE_DURATION = timedelta(hours=0.5)

current_books: List[Dict] = []

placeholder_file_id: str = None
book_images_cache: Dict[int, str] = {}

async def refresh_events() -> None:
    """Refresh events data from the API"""
    global current_events
    try:
        events = await events_repo.get_upcoming_events()
        if events:
            current_events = {event['id']: event for event in events}
            logging.info(f"Events refreshed at {datetime.now()}")
    except Exception as e:
        logging.error(f"Error refreshing events: {e}")

async def get_books(force_refresh: bool = False) -> List[Dict]:
    """Get books from cache or refresh if needed"""
    global current_books

    if current_books is None or force_refresh:
        current_books = await books_repo.get_all_books(db)
    
    return current_books

@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Save user to database
    await user_repo.save_user(
        message.from_user.id,
        message.from_user.username,
        message.from_user.full_name
    )

    if message.from_user.id in settings.ADMINS and message.from_user.id not in user_repo.get_admins():
        user_repo.set_admin(message.from_user.id)

    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")

@dp.message(Command("info"))
async def command_info_handler(message: Message) -> None:
    """
    This handler receives messages with `/info` command
    """
    await message.answer(f"Hi! Here is the info")


@dp.message(Command("events"))
async def command_events_handler(message: Message) -> None:
    """
    This handler receives messages with `/events` command
    """

    
    if not current_events:
        await message.answer("No upcoming events found.")
        return
    
    reply_markup = create_events_keyboard(current_events)
    message_text = f"📅 Upcoming Events"

    await message.answer(message_text, reply_markup=reply_markup)


@dp.callback_query(F.data.startswith("event_"))
async def event_callback_handler(callback: CallbackQuery) -> None:
    """Handle event button clicks"""
    event_id = callback.data.split("_")[1]
    user_id = callback.from_user.id
    event = current_events.get(event_id)
    
    if not event:
        await callback.answer("❌ This event is no longer exists", show_alert=True)
    
    user_reminders = await reminders_repo.get_user_reminders(db, user_id)
    has_reminder = any(r['event_id'] == event_id for r in user_reminders)
    
    message_text = (
        f"*{event['title']}*\n\n"
        f"📅 {format_event_time(event)}\n"
        f"📍 {event['location']}\n\n"
    )
    
    if event.get('url'):
        message_text += f"[Event Link]({event['url']})"
    
    
    await callback.message.edit_text(
        message_text,
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=create_event_details_keyboard(event_id, has_reminder)
    )

@dp.callback_query(F.data == "back_to_events")
async def back_to_events_handler(callback: CallbackQuery) -> None:
    """Handle back button clicks"""
    
    if not current_events:
        await callback.message.edit_text("No events available.")
        return
    
    await callback.message.edit_text(
        f"📅 Upcoming Events",
        reply_markup=create_events_keyboard(current_events)
    )

@dp.message(Command("refresh"))
async def command_refresh_handler(message: Message) -> None:
    """
    This handler receives messages with `/refresh_events` command
    Only admins can use this command
    """
    # Check if user is admin
    if not user_repo.is_admin(message.from_user.id):
        await message.answer("❌ This command is only available for admins.")
        return

    await refresh_events()

    global current_events
    
    if not current_events:
        await message.answer("❌ No upcoming events found after refresh.")
        return
    
    await message.answer("🔄 Events have been refreshed! Use /events to see the updated list.")

@dp.message(Command("reminders"))
async def command_reminders_handler(message: Message) -> None:
    """Show all reminders set by the user"""
    user_id = message.from_user.id
    user_reminders = await reminders_repo.get_user_reminders(db, user_id)
    
    if not user_reminders:
        await message.answer("You don't have any reminders set.")
        return
    
    message_text = "🔔 Your reminders:\n\n"
    for reminder in user_reminders:
        event = current_events.get(reminder['event_id'])
        if event:
            reminder_time = reminder['reminder_time'].astimezone(pytz.timezone('Europe/Helsinki'))
            message_text += (
                f"📅 {event['title']}\n"
                f"⏰ Reminder at: {reminder_time.strftime('%d %b %Y, %H:%M')}\n"
                f"📍 {event['location']}\n\n"
            )
    
    await message.answer(message_text)

@dp.callback_query(F.data.startswith("reminder_"))
async def reminder_callback_handler(callback: CallbackQuery) -> None:
    """Handle reminder button clicks"""
    event_id = callback.data.split("_")[1]
    user_id = callback.from_user.id
    event = current_events.get(event_id)
    
    if not event:
        await callback.answer("Event not found.")
        return
    
    # Check if reminder is already set
    user_reminders = await reminders_repo.get_user_reminders(db, user_id)
    if any(r['event_id'] == event_id for r in user_reminders):
        await callback.answer("You already have a reminder set for this event!")
        return
    
    # Schedule the reminder
    asyncio.create_task(schedule_reminder(callback.bot, user_id, event))

    message_text = (
        f"*{event['title']}*\n\n"
        f"📅 {format_event_time(event)}\n"
        f"📍 {event['location']}\n\n"
    )
    
    if event.get('url'):
        message_text += f"[Event Link]({event['url']})"
    
    await callback.message.edit_text(
        message_text,
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=create_event_details_keyboard(event_id, True)
    )

    await callback.answer("Reminder set! You'll receive a notification 1 hour before the event.")

@dp.callback_query(F.data.startswith("remove_reminder_"))
async def remove_reminder_handler(callback: CallbackQuery) -> None:
    """Handle remove reminder button clicks"""

    event_id = callback.data.split("_")[2]
    user_id = callback.from_user.id
    
    try:
        await reminders_repo.delete_reminder(db, user_id, event_id)
        await callback.answer("Reminder removed!")
    except Exception as e:
        logging.error(f"Error removing reminder: {e}")
        await callback.answer("❌ An error occurred while removing the reminder. Please try again.")

async def periodic_events_refresh() -> None:
    """Periodically refresh events data"""
    while True:
        await asyncio.sleep(EVENTS_CACHE_DURATION.total_seconds())
        await refresh_events()

async def send_reminder(bot: Bot, user_id: int, event: Dict[str, Any]) -> None:
    """Send a reminder message to the user"""
    try:
        message = (
            f"🔔 Reminder: {event['title']} starts in 1 hour!\n\n"
            f"📅 {format_event_time(event)}\n"
            f"📍 {event['location']}"
        )

        await bot.send_message(user_id, message)

        try:    
            await reminders_repo.delete_reminder(db, user_id, event['id'])
        except Exception as e:
            logging.error(f"Reminder doesn't exist in database")
                
    except Exception as e:
        logging.error(f"Error sending reminder: {e}")

async def schedule_reminder(bot: Bot, user_id: int, event: Dict[str, Any]) -> None:
    """Schedule a reminder for the event"""
    try:
        # Calculate time until reminder (1 hour before event)
        now = datetime.now(pytz.UTC)
        reminder_time = event['start_time'] - timedelta(hours=1)
        
        if reminder_time <= now:
            # If event is less than 1 hour away, send reminder immediately
            await send_reminder(bot, user_id, event)
            return
        
        # Save reminder to database
        await reminders_repo.save_reminder(db, user_id, event['id'], reminder_time)
        
        # Calculate delay in seconds
        delay = (reminder_time - now).total_seconds()
        
        # Create and store the reminder task
        task = asyncio.create_task(
            asyncio.sleep(delay),
            name=f"reminder_{event['id']}_{user_id}"
        )
        
        # Wait for the delay and send reminder
        await task
        await send_reminder(bot, user_id, event)
                
    except Exception as e:
        logging.error(f"Error scheduling reminder: {e}")

async def check_reminders(bot: Bot) -> None:
    """Check for reminders that need to be sent"""
    while True:
        try:
            reminders = await reminders_repo.get_reminders(db)
            now = datetime.now(pytz.UTC)
            
            for reminder in reminders:
                if reminder['reminder_time'] <= now:
                    event = current_events.get(reminder['event_id'])
                    if event:
                        await send_reminder(bot, reminder['user_id'], event)
            
            # Check every minute
            await asyncio.sleep(60)
            
        except Exception as e:
            logging.error(f"Error checking reminders: {e}")
            await asyncio.sleep(60)

async def show_books_list(message: Message | CallbackQuery, page: int = 0) -> None:
    """Show paginated list of books"""
    global placeholder_file_id
    
    try:
        # Get books from cache
        books = await get_books()
        
        if not books:
            if isinstance(message, Message):
                await message.answer("No books available.")
            else:
                await message.message.edit_text("No books available.")
            return
        
        # Create keyboard with pagination using the provided page parameter
        reply_markup = create_books_keyboard(books, page)

        if isinstance(message, CallbackQuery):
            # Get the current photo file_id
            current_photo = message.message.photo[-1].file_id if message.message.photo else placeholder_file_id
            
            if placeholder_file_id:
                # Edit the existing photo message
                await message.message.edit_media(
                    media=InputMediaPhoto(
                        media=placeholder_file_id,
                        caption=f"Welcome to Aaltoes Library!"
                    ),
                    reply_markup=reply_markup
                )
            else:
                # First time sending the image
                photo = FSInputFile("images/books_placeholder.png")
                sent_message = await message.message.answer_photo(
                    photo=photo,
                    caption=f"Welcome to Aaltoes Library!",
                    reply_markup=reply_markup
                )
                # Store the file_id for future use
                placeholder_file_id = sent_message.photo[-1].file_id
                # Delete the original message
                await message.message.delete()
        else:
            # If it's a new message, send a photo message
            if placeholder_file_id:
                # Use cached file_id
                await message.answer_photo(
                    photo=placeholder_file_id,
                    caption=f"Welcome to Aaltoes Library!",
                    reply_markup=reply_markup
                )
            else:
                # First time sending the image
                photo = FSInputFile("images/books_placeholder.png")
                sent_message = await message.answer_photo(
                    photo=photo,
                    caption=f"Welcome to Aaltoes Library!",
                    reply_markup=reply_markup
                )
                # Store the file_id for future use
                placeholder_file_id = sent_message.photo[-1].file_id
            
    except Exception as e:
        logging.error(f"Error in show_books_list: {e}")
        if isinstance(message, Message):
            await message.answer("❌ An error occurred while loading the books list. Please try again.")
        else:
            await message.message.answer("❌ An error occurred while loading the books list. Please try again.")

@dp.callback_query(F.data.startswith("instance_select_"))
async def book_instance_select_handler(callback: CallbackQuery) -> None:
    """Handle book instance selection"""
    book_id = int(callback.data.split("_")[2])
        
    books = await get_books(force_refresh=True) 

    book = next((b for b in books if b['book_id'] == book_id), None)
    if not book:
        await callback.answer("Book not found", show_alert=True)
        return
        
    instances = await books_repo.get_book_instances(db, book_id)

    if not instances:
        await callback.answer("No instances found", show_alert=True)
        return
        
    # Filter available instances
    available_instances = [i for i in instances if i['available']]

    if not available_instances:
        await callback.answer("No available copies", show_alert=True)
        return
    
    current_page = callback.data.split("_")[-1]
    keyboard = create_instance_selection_keyboard(available_instances, book_id, current_page)

    await callback.message.edit_caption(
        caption="Select a copy to borrow:",
        reply_markup=keyboard
    )
    

@dp.callback_query(F.data.startswith("instance_"))
async def book_instance_handler(callback: CallbackQuery) -> None:
    """Handle book instance selection"""
    try:
        # Get instance_id and book_id from callback data
        # Format: book_instance_{instance_id}_{book_id}
        parts = callback.data.split("_")
        instance_id = int(parts[1])
        book_id = int(parts[2])
        
        # Get current instance status
        instances = await books_repo.get_book_instances(db, book_id)
        instance = next((i for i in instances if i['instance_id'] == instance_id), None)
        
        if not instance:
            await callback.answer("❌ Instance not found", show_alert=True)
            return
            
        if not instance['available']:
            await callback.answer("❌ This copy is no longer available", show_alert=True)
            return
        
        # Update instance availability
        await books_repo.update_book_availability(db, instance_id, False)
        
        # Get book details for success message
        books = await get_books(force_refresh=True)  # Refresh to get updated availability
        book = next((b for b in books if b['book_id'] == book_id), None)
        
        success_message = (
            f"✅ Successfully borrowed\n\n"
            f"📚 {book['title']}\n"
            f"👤 Author: {book.get('author', 'Unknown')}\n"
            f"📖 Copy #{instance_id}\n\n"
            f"🔔 Reminder: You have 14 days to return the book.\n\n"
            f"Back to library /books"
        )
    
        await callback.message.edit_media(
            media=InputMediaPhoto(
                media=callback.message.photo[-1].file_id,
                caption=success_message
            )
        )
 
    except Exception as e:
        logging.error(f"Error in book_instance_handler: {e}")
        logging.error(f"Callback data: {callback.data}")
        await callback.answer("❌ An error occurred while booking the copy. Please try again.")

@dp.callback_query(F.data.startswith("books_page_"))
async def books_page_handler(callback: CallbackQuery) -> None:
    """Handle books pagination"""
    try:
        # Get page number from callback data
        page = int(callback.data.split("_")[2])
        logging.info(f"Handling page navigation to page {page}")
        
        # Get books from cache without forcing refresh
        books = await get_books(force_refresh=False)

        if not books:
            await callback.answer("No books available", show_alert=True)
            return
            
        reply_markup = create_books_keyboard(books, page)
        
        await callback.message.edit_media(
            media=InputMediaPhoto(
                media=placeholder_file_id,
                caption=f"Welcome to Aaltoes Library! "
            ),
            reply_markup=reply_markup
        )
            
    except Exception as e:
        logging.error(f"Error in books_page_handler: {str(e)}")
        logging.error(f"Callback data: {callback.data}")
        await callback.answer("An error occurred while changing pages", show_alert=True)

@dp.callback_query(F.data.startswith("book_"))
async def book_callback_handler(callback: CallbackQuery) -> None:
    """Handle book button clicks"""
        
    
    parts = callback.data.split("_")
    logging.info(f"Received book callback: {parts}")
    book_id = int(parts[1])
    current_page = int(parts[2]) if len(parts) > 2 else 0
    
    # Get books from cache without forcing refresh
    books = await get_books(force_refresh=False)
    book = next((b for b in books if b['book_id'] == book_id), None)
    
    # Get book instances
    instances = await books_repo.get_book_instances(db, book_id)
    
    # Build message text with optional fields
    message_text = f"📚 *{book.get('title', 'No title available')}*\n\n"
    
    if book.get('author'):
        message_text += f"👤 Author: {book['author']}\n"
    
    if book.get('year'):
        message_text += f"📅 Year: {book['year']}\n"
    
    # Add availability info from instances
    total_instances = len(instances)
    available_instances = sum(1 for i in instances if i['available'])
    message_text += f"📖 Copies: {available_instances}/{total_instances} available\n\n"
    
    if book.get('description'):
        message_text += f"{book['description']}\n\n"

    image_path = None
    if instances and instances[0].get('image'):
        image_path = instances[0]['image']
    
        if book_id in book_images_cache:
            # Use cached file_id
            await callback.message.edit_media(
                media=InputMediaPhoto(
                    media=book_images_cache[book_id],
                    caption=message_text,
                    parse_mode=ParseMode.MARKDOWN
                ),
                reply_markup=create_book_details_keyboard(book_id, current_page, available_instances)
            )
        else:
            # First time sending this image
            photo = FSInputFile(image_path)
            sent_message = await callback.message.edit_media(
                media=InputMediaPhoto(
                    media=photo,
                    caption=message_text,
                    parse_mode=ParseMode.MARKDOWN
                ),
                reply_markup=create_book_details_keyboard(book_id, current_page, available_instances)
            )
            # Store the file_id for future use
            book_images_cache[book_id] = sent_message.photo[-1].file_id



@dp.message(Command("books"))
async def command_books_handler(message: Message) -> None:
    """Handle /books command"""
    try:
        # Force refresh books if cache is stale
        books = await get_books(force_refresh=True)
        if not books:
            await message.answer("❌ No books available at the moment. Please try again later.")
            return
            
        await show_books_list(message)

    except Exception as e:
        logging.error(f"Error in /books command: {e}")
        await message.answer("❌ An error occurred while loading the books. Please try again.")


async def main() -> None:
    
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    # Connect to the database
    await db.connect(settings.DATABASE_URL_UNPOOLED)
    # Initialize tables
    await user_repo.init(db)
    await reminders_repo.init(db)
    await books_repo.init(db)
    # Start periodic events refresh
    asyncio.create_task(periodic_events_refresh())
    
    # Start reminders checker
    asyncio.create_task(check_reminders(bot))
    
    # And the run events dispatching
    try:
        await dp.start_polling(bot)
    finally:
        # Close the database connection when the bot is stopped
        await db.close()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())