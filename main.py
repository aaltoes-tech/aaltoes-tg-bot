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

# Initialize timezone finder
tf = TimezoneFinder()

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

# Store events data in memory with timestamp
current_events: Dict[str, Dict] = {}
last_events_update: datetime = None
EVENTS_CACHE_DURATION = timedelta(hours=1)  # Cache events for 1 hour

# Store books data in memory with timestamp
current_books: List[Dict] = []
last_books_update: datetime = None
BOOKS_CACHE_DURATION = timedelta(hours=1)  # Cache books for 1 hour
books_cache_lock = asyncio.Lock()  # Add a lock for thread-safe cache updates
placeholder_file_id: str = None  # Store Telegram's file_id for the placeholder image
book_images_cache: Dict[int, str] = {}  # Store file_ids for book images

async def refresh_events() -> None:
    """Refresh events data from the API"""
    global current_events, last_events_update
    try:
        events = await events_repo.get_upcoming_events()
        if events:
            current_events = {event['id']: event for event in events}
            last_events_update = datetime.now()
            logging.info(f"Events refreshed at {last_events_update}")
    except Exception as e:
        logging.error(f"Error refreshing events: {e}")

async def get_events() -> Tuple[Dict[str, Dict], bool]:
    """
    Get events from cache or refresh if needed
    Returns: (events_dict, was_refreshed)
    """
    global current_events, last_events_update
    
    if not last_events_update or datetime.now() - last_events_update > EVENTS_CACHE_DURATION:
        await refresh_events()
        return current_events, True
    return current_events, False

async def get_books(force_refresh: bool = False) -> Tuple[List[Dict], bool]:
    """Get books from cache or database if cache is stale or force_refresh is True"""
    global current_books, last_books_update
    
    async with books_cache_lock:
        now = datetime.now()
        if force_refresh or not current_books or not last_books_update or (now - last_books_update) > BOOKS_CACHE_DURATION:
            try:
                logging.info("Refreshing books cache")
                current_books = await books_repo.get_all_books(db)
                last_books_update = now
                logging.info(f"Successfully refreshed {len(current_books)} books")
                logging.info(f"Books data: {current_books[:2]}")  # Log first two books for debugging
                return current_books, True
            except Exception as e:
                logging.error(f"Error refreshing books: {e}")
                return current_books, False
        logging.debug("Using cached books data")
        logging.info(f"Using cached books: {len(current_books)} books")
        return current_books, False

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
    events, was_refreshed = await get_events()
    
    if not events:
        await message.answer("No upcoming events found.")
        return
    
    reply_markup = create_events_keyboard(events)
    refresh_time = last_events_update.astimezone(pytz.timezone('Europe/Helsinki'))
    refresh_str = refresh_time.strftime("%d %b %Y, %H:%M")
    message_text = f"📅 Upcoming Events\nLast updated: {refresh_str}"

    await message.answer(message_text, reply_markup=reply_markup)

@dp.callback_query(F.data.startswith("event_"))
async def event_callback_handler(callback: CallbackQuery) -> None:
    """Handle event button clicks"""
    event_id = callback.data.split("_")[1]
    user_id = callback.from_user.id
    events, _ = await get_events()
    event = events.get(event_id)
    
    if not event:
        await callback.message.edit_text(
            "Event not found. Please try again.",
            reply_markup=create_back_to_events_keyboard()
        )
        return
    
    # Check if user has a reminder for this event
    user_reminders = await reminders_repo.get_user_reminders(db, user_id)
    has_reminder = any(r['event_id'] == event_id for r in user_reminders)
    
    message_text = (
        f"*{event['title']}*\n\n"
        f"📅 {format_event_time(event)}\n"
        f"📍 {event['location']}\n\n"
    )
    
    if event.get('url'):
        message_text += f"[Event Link]({event['url']})"
    
    try:
        await callback.message.edit_text(
            message_text,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=create_event_details_keyboard(event_id, has_reminder)
        )
    except Exception as e:
        # Fallback to HTML if Markdown fails
        message_text = (
            f"<b>{event['title']}</b>\n\n"
            f"📅 {format_event_time(event)}\n"
            f"📍 {event['location']}\n\n"
        )
        
        if event.get('url'):
            message_text += f"<a href='{event['url']}'>Event Link</a>"
        
        await callback.message.edit_text(
            message_text,
            parse_mode=ParseMode.HTML,
            reply_markup=create_event_details_keyboard(event_id, has_reminder)
        )

@dp.callback_query(F.data == "back_to_events")
async def back_to_events_handler(callback: CallbackQuery) -> None:
    """Handle back button clicks"""
    events, _ = await get_events()
    
    if not events:
        await callback.message.edit_text("No events available. Please use /events command.")
        return
    
    await callback.message.edit_text(
        f"📅 Upcoming Events\nLast updated: {last_events_update.astimezone(pytz.timezone('Europe/Helsinki')).strftime('%d %b %Y, %H:%M')}",
        reply_markup=create_events_keyboard(events)
    )

@dp.message(Command("refresh_events"))
async def command_refresh_events_handler(message: Message) -> None:
    """
    This handler receives messages with `/refresh_events` command
    Only admins can use this command
    """
    # Check if user is admin
    if not user_repo.is_admin(message.from_user.id):
        await message.answer("❌ This command is only available for admins.")
        return
    
    # Refresh events
    await refresh_events()
    
    # Get the updated events
    events, _ = await get_events()
    
    if not events:
        await message.answer("No upcoming events found after refresh.")
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
    
    # Get current events to match with reminders
    events, _ = await get_events()
    
    message_text = "🔔 Your reminders:\n\n"
    for reminder in user_reminders:
        event = events.get(reminder['event_id'])
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
    events, _ = await get_events()
    event = events.get(event_id)
    
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
    
    # Update the message with the new keyboard
    message_text = (
        f"*{event['title']}*\n\n"
        f"📅 {format_event_time(event)}\n"
        f"📍 {event['location']}\n\n"
    )
    
    if event.get('url'):
        message_text += f"[Event Link]({event['url']})"
    
    try:
        await callback.message.edit_text(
            message_text,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=create_event_details_keyboard(event_id, True)
        )
    except Exception as e:
        # Fallback to HTML if Markdown fails
        message_text = (
            f"<b>{event['title']}</b>\n\n"
            f"📅 {format_event_time(event)}\n"
            f"📍 {event['location']}\n\n"
        )
        
        if event.get('url'):
            message_text += f"<a href='{event['url']}'>Event Link</a>"
        
        await callback.message.edit_text(
            message_text,
            parse_mode=ParseMode.HTML,
            reply_markup=create_event_details_keyboard(event_id, True)
        )
    
    await callback.answer("Reminder set! You'll receive a notification 1 hour before the event.")

@dp.callback_query(F.data.startswith("remove_reminder_"))
async def remove_reminder_handler(callback: CallbackQuery) -> None:
    """Handle remove reminder button clicks"""
    event_id = callback.data.split("_")[2]
    user_id = callback.from_user.id
    
    # Delete the reminder from the database
    await reminders_repo.delete_reminder(db, user_id, event_id)
    
    # Get the event details to show updated keyboard
    events, _ = await get_events()
    event = events.get(event_id)
    
    if event:
        message_text = (
            f"*{event['title']}*\n\n"
            f"📅 {format_event_time(event)}\n"
            f"📍 {event['location']}\n\n"
        )
        
        if event.get('url'):
            message_text += f"[Event Link]({event['url']})"
        
        try:
            await callback.message.edit_text(
                message_text,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=create_event_details_keyboard(event_id, False)
            )
        except Exception as e:
            # Fallback to HTML if Markdown fails
            message_text = (
                f"<b>{event['title']}</b>\n\n"
                f"📅 {format_event_time(event)}\n"
                f"📍 {event['location']}\n\n"
            )
            
            if event.get('url'):
                message_text += f"<a href='{event['url']}'>Event Link</a>"
            
            await callback.message.edit_text(
                message_text,
                parse_mode=ParseMode.HTML,
                reply_markup=create_event_details_keyboard(event_id, False)
            )
    
    await callback.answer("Reminder removed!")

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
        
        # Delete the reminder from the database after sending
        await reminders_repo.delete_reminder(db, user_id, event['id'])
                
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
                    events, _ = await get_events()
                    event = events.get(reminder['event_id'])
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
        books, _ = await get_books()
        
        if not books:
            if isinstance(message, Message):
                await message.answer("No books available.")
            else:
                await message.message.edit_text("No books available.")
            return
        
        # Create keyboard with pagination using the provided page parameter
        reply_markup = create_books_keyboard(books, page)
        logging.info(f"Creating books keyboard for page {page}")
        
        if isinstance(message, CallbackQuery):
            # Get the current photo file_id
            current_photo = message.message.photo[-1].file_id if message.message.photo else placeholder_file_id
            
            if current_photo:
                # Edit the existing photo message
                await message.message.edit_media(
                    media=InputMediaPhoto(
                        media=current_photo,
                        caption=f"Welcome to Aaltoes Library! (Page {page + 1})"
                    ),
                    reply_markup=reply_markup
                )
            else:
                # First time sending the image
                photo = FSInputFile("images/books_placeholder.png")
                sent_message = await message.message.answer_photo(
                    photo=photo,
                    caption=f"Welcome to Aaltoes Library! (Page {page + 1})",
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
                    caption=f"Welcome to Aaltoes Library! (Page {page + 1})",
                    reply_markup=reply_markup
                )
            else:
                # First time sending the image
                photo = FSInputFile("images/books_placeholder.png")
                sent_message = await message.answer_photo(
                    photo=photo,
                    caption=f"Welcome to Aaltoes Library! (Page {page + 1})",
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

@dp.callback_query(F.data.startswith("book_instance_select_"))
async def book_instance_select_handler(callback: CallbackQuery) -> None:
    """Handle book instance selection"""
    logging.info(f"Received instance selection callback: {callback.data}")
    try:
        # Extract book ID from callback data
        book_id = int(callback.data.split("_")[3])
        logging.info(f"Handling instance selection for book {book_id}")
        
        # Get book details and instances
        books, _ = await get_books(force_refresh=True)  # Refresh to get latest availability
        book = next((b for b in books if b['book_id'] == book_id), None)
        if not book:
            logging.error(f"Book {book_id} not found")
            await callback.answer("Book not found", show_alert=True)
            return
            
        instances = await books_repo.get_book_instances(db, book_id)
        logging.info(f"Found {len(instances)} instances for book {book_id}")
        if not instances:
            logging.error(f"No instances found for book {book_id}")
            await callback.answer("No instances found", show_alert=True)
            return
            
        # Filter available instances
        available_instances = [i for i in instances if i['available']]
        logging.info(f"Found {len(available_instances)} available instances")
        if not available_instances:
            logging.error(f"No available instances for book {book_id}")
            await callback.answer("No available copies", show_alert=True)
            return
            
        # Create instance selection keyboard
        keyboard = []
        for instance in available_instances:
            keyboard.append([
                InlineKeyboardButton(
                    text=f"Copy #{instance['instance_id']}",
                    callback_data=f"book_instance_{instance['instance_id']}_{book_id}"
                )
            ])
        
        current_page = callback.data.split("_")[-1]
            
        # Add back button
        keyboard.append([
            InlineKeyboardButton(
                text="⬅️ Back to Book",
                callback_data=f"book_{book_id}_{current_page}"  # Added page number for back navigation
            )
        ])
        
        # Edit message to show instance selection
        if callback.message.photo:
            await callback.message.edit_caption(
                caption="Select a copy to borrow:",
                reply_markup=InlineKeyboardMarkup(inline_keyboard=keyboard)
            )
        else:
            await callback.message.edit_text(
                text="Select a copy to borrow:",
                reply_markup=InlineKeyboardMarkup(inline_keyboard=keyboard)
            )
            
    except Exception as e:
        logging.error(f"Error in book_instance_select_handler: {str(e)}")
        logging.error(f"Callback data: {callback.data}")
        await callback.answer("An error occurred", show_alert=True)

@dp.callback_query(F.data.startswith("book_instance_"))
async def book_instance_handler(callback: CallbackQuery) -> None:
    """Handle book instance selection"""
    logging.info(f"Received instance selection callback: {callback.data}")
    try:
        # Get instance_id and book_id from callback data
        # Format: book_instance_{instance_id}_{book_id}
        parts = callback.data.split("_")
        instance_id = int(parts[2])
        book_id = int(parts[3])
        logging.info(f"Processing instance {instance_id} for book {book_id}")
        
        # Update instance availability
        await books_repo.update_book_availability(db, instance_id, False)
        logging.info(f"Updated availability for instance {instance_id}")
        
        # Get book details for success message
        books, _ = await get_books(force_refresh=True)  # Refresh to get updated availability
        book = next((b for b in books if b['book_id'] == book_id), None)
        logging.info(f"Found book: {book}")
        
        if book:
            success_message = (
                f"✅ Successfully borrowed\n\n"
                f"📚 {book['title']}\n"
                f"👤 Author: {book.get('author', 'Unknown')}\n"
                f"📖 Copy #{instance_id}\n\n"
                f"🔔 Reminder: You have 14 days to return the book.\n\n"
                f"Back to library /books"
            )
        else:
            success_message = "✅ Successfully borrowed the book!"
        
            
        # Get the current image file_id from the message
        current_photo = callback.message.photo[-1].file_id if callback.message.photo else None
        
        if current_photo:
            # Edit the existing photo message with success message
            await callback.message.edit_media(
                media=InputMediaPhoto(
                    media=current_photo,
                    caption=success_message
                )
            )
        else:
            # If no photo, just send text message
            await callback.message.delete()
            await callback.message.answer(success_message)
            
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
        books, _ = await get_books(force_refresh=False)

        if not books:
            await callback.answer("No books available", show_alert=True)
            return
            
        # Create keyboard with pagination
        reply_markup = create_books_keyboard(books, page)
        
        # Edit the message with new keyboard
        if callback.message.photo:
            # Get the current photo file_id
            current_photo = callback.message.photo[-1].file_id
            await callback.message.edit_media(
                media=InputMediaPhoto(
                    media=current_photo,
                    caption=f"Welcome to Aaltoes Library! "
                ),
                reply_markup=reply_markup
            )
        else:
            await callback.message.edit_text(
                text=f"Welcome to Aaltoes Library!",
                reply_markup=reply_markup
            )
            
    except Exception as e:
        logging.error(f"Error in books_page_handler: {str(e)}")
        logging.error(f"Callback data: {callback.data}")
        await callback.answer("An error occurred while changing pages", show_alert=True)


@dp.message(Command("books"))
async def command_books_handler(message: Message) -> None:
    """Handle /books command"""
    try:
        # Force refresh books if cache is stale
        books, refreshed = await get_books(force_refresh=True)
        if not books:
            await message.answer("❌ No books available at the moment. Please try again later.")
            return
            
        if refreshed:
            logging.info("Refreshed books cache")
        await show_books_list(message)
    except Exception as e:
        logging.error(f"Error in /books command: {e}")
        await message.answer("❌ An error occurred while loading the books. Please try again.")

@dp.callback_query(F.data.startswith("book_"))
async def book_callback_handler(callback: CallbackQuery) -> None:
    """Handle book button clicks"""
    logging.info(f"Book callback received: {callback.data}")
        
    # Get book_id and current page from callback data
    # Format: book_{book_id}_{page}
    parts = callback.data.split("_")
    book_id = int(parts[1])
    current_page = int(parts[2]) if len(parts) > 2 else 0
    
    # Get books from cache without forcing refresh
    books, _ = await get_books(force_refresh=False)
    book = next((b for b in books if b['book_id'] == book_id), None)
    
    if not book:
        # Check if the current message is a photo or text
        if callback.message.photo:
            await callback.message.edit_caption(
                caption="Book not found. Please try again.",
                reply_markup=create_book_details_keyboard(book_id, current_page, 0)
            )
        else:
            await callback.message.edit_text(
                "Book not found. Please try again.",
                reply_markup=create_book_details_keyboard(book_id, current_page, 0)
            )
        return
    
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

    try:
        # Get image from the first instance
        image_path = None
        if instances and instances[0].get('image'):
            image_path = instances[0]['image']
        
        # Check if the current message is a photo or text
        if callback.message.photo:
            if image_path:
                # Check if we have a cached file_id for this image
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
            else:
                # If no image, just edit the caption
                await callback.message.edit_caption(
                    caption=message_text,
                    parse_mode=ParseMode.MARKDOWN,
                    reply_markup=create_book_details_keyboard(book_id, current_page, available_instances)
                )
        else:
            # If it's a text message, just edit the text
            await callback.message.edit_text(
                message_text,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=create_book_details_keyboard(book_id, current_page, available_instances)
            )
    except Exception as e:
        logging.error(f"Error sending book details: {e}")
        logging.error(f"Book data: {book}")
        # Check if the current message is a photo or text
        if callback.message.photo:
            await callback.message.edit_caption(
                caption="Sorry, there was an error displaying the book details. Please try again.",
                reply_markup=create_book_details_keyboard(book_id, current_page, available_instances)
            )
        else:
            await callback.message.edit_text(
                "Sorry, there was an error displaying the book details. Please try again.",
                reply_markup=create_book_details_keyboard(book_id, current_page, available_instances)
            )

@dp.callback_query(F.data.startswith("return_to_books_"))
async def return_to_books_handler(callback: CallbackQuery) -> None:
    """Handle return to books button click"""
    global placeholder_file_id
    
    try:
        # Get the page number from the callback data
        # Format: return_to_books_{book_id}_{page}
        parts = callback.data.split("_")
        if len(parts) >= 4:
            page = int(parts[3])
        else:
            page = 0
            
        # Get books from cache (no refresh needed for back navigation)
        books, _ = await get_books(force_refresh=False)
        if not books:
            await callback.message.edit_text(
                "No books available. Please use /books command.",
                reply_markup=create_books_keyboard([], 0)
            )
            return
        
        # Always edit the photo message
        if placeholder_file_id:
            await callback.message.edit_media(
                media=InputMediaPhoto(
                    media=placeholder_file_id,
                    caption=f"Welcome to Aaltoes Library! (Page {page + 1})"
                ),
                reply_markup=create_books_keyboard(books, page)
            )
        else:
            # If no cached file_id, send a new photo message
            photo = FSInputFile("images/books_placeholder.png")
            sent_message = await callback.message.answer_photo(
                photo=photo,
                caption=f"Welcome to Aaltoes Library! (Page {page + 1})",
                reply_markup=create_books_keyboard(books, page)
            )
            # Store the file_id for future use
            placeholder_file_id = sent_message.photo[-1].file_id
            # Delete the original message
            await callback.message.delete()
            
    except Exception as e:
        logging.error(f"Error in return_to_books_handler: {e}")
        # Get books again to ensure we have data for the keyboard
        books, _ = await get_books(force_refresh=False)
        await callback.message.edit_text(
            "❌ An error occurred while going back to the books list. Please try again.",
            reply_markup=create_books_keyboard(books, 0)
        )

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