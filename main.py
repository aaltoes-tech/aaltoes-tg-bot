import asyncio
import logging
import sys
from datetime import datetime, timedelta
from typing import Dict, List, Tuple, Any

import pytz

from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters.command import Command
from aiogram.types import Message, CallbackQuery, FSInputFile, InputMediaPhoto
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from settings import settings
from db import db
from repository.user import UserRepository
from repository.events import EventsRepository
from repository.reminders import RemindersRepository
from repository.books import BooksRepository
from repository.borrowings import BorrowingsRepository
from keyboards import create_events_keyboard, create_event_details_keyboard, create_books_keyboard, create_book_details_keyboard, create_instance_selection_keyboard, create_pending_borrowings_keyboard,create_approve_borrowing_keyboard, create_return_keyboard


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
borrowings_repo = BorrowingsRepository()

# Initialize storage
storage = MemoryStorage()

# Initialize dispatcher
dp = Dispatcher(storage=storage)

current_events: Dict[str, Dict] = {}
EVENTS_CACHE_DURATION = timedelta(hours=0.5)
OVERDUE_CHECK_INTERVAL = timedelta(hours=1)
OVERDUE_NOTIFICATION_INTERVAL = timedelta(hours=12)
pending_borrowings: List[Dict] = []

current_books: List[Dict] = []

placeholder_file_id: str = None
placeholder_file_id_2: str = None

# Use Pinata's image optimization with reduced size (300px width) and WebP format
placeholder_file_1_url = 'https://amaranth-defiant-snail-192.mypinata.cloud/ipfs/bafybeiawgmucvhow67n6xclzly2zxb6hgchwgacgljdh6iprzzwlebkwqe?img-width=500&img-quality=80&img-format=webp'
placeholder_file_2_url = 'https://amaranth-defiant-snail-192.mypinata.cloud/ipfs/bafkreiberkd4tzafmhmsepnwbtw32ois4b4enfvcl23hoo6bbkhrmz2moe?img-width=500&img-quality=80&img-format=webp'

def get_optimized_image_url(ipfs_url: str) -> str:
    """Get optimized image URL from Pinata IPFS URL"""
    if not ipfs_url or not ipfs_url.startswith('https://'):
        return ipfs_url
    # Add optimization parameters if not already present
    if '?img-width=' not in ipfs_url:
        return f"{ipfs_url}?img-width=500&img-quality=80&img-format=webp"
    return ipfs_url

class BorrowState(StatesGroup):
    SELECT_INSTANCE = State()  # Only need this state for direct instance input
    RETURN_BOOK = State()

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

    welcome_message = (
        f"👋 Hello, {html.bold(message.from_user.full_name)}!\n\n"
        f"Welcome to the Aaltoes Community Bot! \n\n"
        f"Type /help to see all available commands!"
    )

    await message.answer(welcome_message)

@dp.message(Command("help"))
async def command_help_handler(message: Message) -> None:
    """
    This handler receives messages with `/help` command
    """
    help_message = "List of available commands:\n\n"
    help_message += "/info - Show information about Aaltoes\n"
    help_message += "/events - Show upcoming events\n"
    help_message += "/reminders - Show your event reminders\n"
    help_message += "/books - Show available books\n"
    help_message += "/borrow - Borrow a book\n"
    help_message += "/return - Return a book\n"
    help_message += "/borrowings - Show your borrowings\n"
    help_message += "/history - Show your borrowing history\n"

    await message.answer(help_message)

@dp.message(Command("info"))
async def command_info_handler(message: Message) -> None:
    """
    This handler receives messages with `/info` command
    """
    info_message = (
        "🌟 *About Aaltoes*\n\n"
        "Aaltoes (Aalto Entrepreneurship Society) is the largest student-run entrepreneurship community in Northern Europe. "
        "We are a non-profit organization that helps students and young professionals to develop their entrepreneurial skills "
        "and build their own businesses.\n\n"
        "*Connect with us:*\n"
        "Website: [aaltoes.com](https://aaltoes.com)\n"
        "Instagram: [@aaltoes](https://www.instagram.com/aaltoes/)\n"
        "LinkedIn: [Aaltoes](https://www.linkedin.com/company/aaltoes/)\n"
        "Facebook: [Aaltoes](https://www.facebook.com/aaltoes/)\n"
        "Twitter: [@Aaltoes](https://twitter.com/Aaltoes)\n"
        "Telegram: [@aaltoes](https://t.me/aaltoes)\n\n"
        "📍 *Location:*\n"
        "Aaltoes Startup Sauna\n"
        "Otakaari 5, 02150 Espoo, Finland"
    )
    
    await message.answer(info_message, parse_mode=ParseMode.MARKDOWN)


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

    user = await user_repo.get_user(message.from_user.id)
    if user['role'] != 'admin':
        await message.answer("You are not authorized to use this command.")
    else:
   
        await refresh_events()
        global current_events
    
        if not current_events:
            await message.answer("❌ No upcoming events found after refresh.")
            return
        else:
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
            
            if reminders:
                for reminder in reminders:
                    if reminder['reminder_time'] <= now:
                        event = current_events.get(reminder['event_id'])
                    if event:
                        await send_reminder(bot, reminder['user_id'], event)
            await asyncio.sleep(60)
            
        except Exception as e:
            logging.error(f"Error checking reminders: {e}")
            logging.error(f"Reminders: {reminders}")
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
                # First time sending the image - use optimized URL
                sent_message = await message.message.edit_media(
                    media=InputMediaPhoto(
                        media=get_optimized_image_url(placeholder_file_1_url),
                        caption=f"Welcome to Aaltoes Library!",
                        reply_markup=reply_markup
                    )
                )
                # Store the file_id for future use
                placeholder_file_id = sent_message.photo[-1].file_id
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
                # First time sending the image - use optimized URL
                sent_message = await message.answer_photo(
                    photo=get_optimized_image_url(placeholder_file_1_url),
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

async def update_overdue_borrowings(bot: Bot) -> None:
    """Check for borrowings that need to be returned"""
    while True:
        await asyncio.sleep(OVERDUE_CHECK_INTERVAL.total_seconds())
        await borrowings_repo.update_overdue_borrowings(db)

async def send_overdue_notification(bot: Bot) -> None:
    """Send a notification to the user that their borrowing is overdue"""
    while True:
        await asyncio.sleep(OVERDUE_NOTIFICATION_INTERVAL.total_seconds())
        overdue_borrowings = await borrowings_repo.get_overdue_borrowings(db)
        for borrowing in overdue_borrowings:
            await bot.send_message(borrowing['user_id'], f"Copy #{borrowing['instance_id']} is overdue. Please return it to the library.")
            

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
        
        # Check if user has already borrowed this book
        borrowings = await borrowings_repo.get_user_borrowings(db, callback.from_user.id)

        if len(borrowings) >= 3:
            await callback.answer("❌ You have reached the maximum number of borrowings (3)", show_alert=True)
            return
        
        # Create borrowing record
        borrow_id = await borrowings_repo.create_borrowing(db, callback.from_user.id, instance_id)
        
        # Update instance availability
        await books_repo.update_book_availability(db, instance_id, False)
        
        # Get book details for success message
        books = await get_books(force_refresh=True)  # Refresh to get updated availability
        book = next((b for b in books if b['book_id'] == book_id), None)
        
        # Get borrowing details
        borrowing = await borrowings_repo.get_borrowing_by_instance(db, instance_id)
        return_time = borrowing['borrow_return_time'].strftime('%d %b %Y')
        
        success_message = (
            f"✅ Successfully borrowed\n\n"
            f"📚 {book['title']}\n"
            f"👤 Author: {book.get('author', 'Unknown')}\n"
            f"📖 Copy #{instance_id}\n"
            f"📅 Return by: {return_time}\n\n"
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
    global placeholder_file_id_2

    parts = callback.data.split("_")
    book_id = int(parts[1])
    current_page = int(parts[2]) if len(parts) > 2 else 0
    
    # Get books from cache without forcing refresh
    books = await get_books(force_refresh=False)
    book = next((b for b in books if b['book_id'] == book_id), None)
    
    # Get book instances
    instances = await books_repo.get_book_instances(db, book_id)
    instance_id = instances[0]['instance_id']
    
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
        file_id = await books_repo.get_file_id(db, instance_id)
        await callback.message.edit_media(
            media=InputMediaPhoto(
                media=file_id,
                caption=message_text,
                parse_mode=ParseMode.MARKDOWN
            ),
            reply_markup=create_book_details_keyboard(book_id, current_page, available_instances)
        )
    except Exception as e:


        try:    
            image_path = instances[0]['image']
            sent_message = await callback.message.edit_media(
                media=InputMediaPhoto(
                media=get_optimized_image_url(image_path),
                caption=message_text,
                parse_mode=ParseMode.MARKDOWN
            ),
            reply_markup=create_book_details_keyboard(book_id, current_page, available_instances)
        )
                    # Store the file_id in both memory and database
            file_id = sent_message.photo[-1].file_id
            await books_repo.save_file_id(db, instance_id, file_id)
        except Exception as e:
            if placeholder_file_id_2:
                # Use cached placeholder
                await callback.message.edit_media(
                    media=InputMediaPhoto(
                        media=placeholder_file_id_2,
                        caption=message_text,
                        parse_mode=ParseMode.MARKDOWN
                    ),
                    reply_markup=create_book_details_keyboard(book_id, current_page, available_instances)
                )
            else:
                # First time sending placeholder - use optimized URL
                sent_message = await callback.message.edit_media(
                    media=InputMediaPhoto(
                        media=get_optimized_image_url(placeholder_file_2_url),
                        caption=message_text,
                        parse_mode=ParseMode.MARKDOWN
                    ),
                    reply_markup=create_book_details_keyboard(book_id, current_page, available_instances)
                )
                placeholder_file_id_2 = sent_message.photo[-1].file_id

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

@dp.message(Command("borrowings"))
async def command_borrowings_handler(message: Message) -> None:
    """Handle /borrowings command"""
    borrowings = await borrowings_repo.get_user_borrowings(db, message.from_user.id)
    
    text = f"You have {len(borrowings)} active borrowings."

    if len(borrowings) > 0:    
        text += "Press /return to return the book\n------------------------------\n"


    for borrowing in borrowings:
        logging.info(f"Processing borrowing: {borrowing}")
        text += f"📚 {borrowing['title']}\n"
        text += f"👤 Author: {borrowing['author']}\n"
        text += f"🖼️ Copy #{borrowing['instance_id']}\n"
        text += f"Return by: {borrowing['borrow_return_time']}\n"
        text += f"State: "
        if borrowing['state'] == 'overdue':
            text += "❌ Overdue\n"
        elif borrowing['state'] == 'pending':
            text += "⏳ Pending\n"
        elif borrowing['state'] == 'borrowed':
            text += "🤝 Borrowed\n"
        elif borrowing['state'] == 'returned':
            text += "✅ Returned\n"
        text +="------------------------------\n"
    pending_borrowings = await borrowings_repo.get_user_pending_borrowings(db, message.from_user.id)
    if pending_borrowings:
        m = len(pending_borrowings)

        for i, book in  enumerate(pending_borrowings):
            text+=f"Book #{book['instance_id']}"
            if i < m-1:
                text+=","
        if m>1:
            text+=" are still pending"
        else:
            text+=" is still pending"
    
    await message.answer(text)

@dp.message(Command("admin"))
async def command_admin_handler(message: Message) -> None:
    """Handle /admin command"""
    user = await user_repo.get_user(message.from_user.id)
    if user['role'] != 'admin':
        await message.answer("You are not authorized to use this command.")
    else:
        admin_commands = (
            "Admin Commands:\n\n"
            "/refresh - Refresh events list\n"
            "/refresh_books - Refresh books list\n"
            "/check - Check pending borrowings\n"
            "/admin - Show this help message\n\n"

        )
        await message.answer(admin_commands)
   
@dp.message(Command("history"))
async def command_history_handler(message: Message) -> None:
    """Handle /history command"""
    borrowings = await borrowings_repo.get_user_borrowings_history(db, message.from_user.id)
    if not borrowings:
        await message.answer("You have no borrowings.")
        return
    text = f"Your borrowing history:\n"
    for i, borrowing in enumerate(borrowings):
        text+=f"{i+1}. Time: {borrowing['borrow_time']}, "
        text+=f"Copy #{borrowing['instance_id']}\n"
    await message.answer(text)
@dp.message(Command("return"))
async def command_return_handler(message: Message, state: FSMContext) -> None:
    """Handle /return command"""
    borrowings = await borrowings_repo.get_user_borrowings(db, message.from_user.id)
    if not borrowings:
        await message.answer("You have no borrowings.")
        return
    
    await message.answer(
        "📚 Please select the book you want to return:",
        reply_markup=create_return_keyboard(borrowings)
    )
    await state.set_state(BorrowState.RETURN_BOOK)

@dp.message(BorrowState.RETURN_BOOK)
async def process_return_book(message: Message, state: FSMContext) -> None:
    """Process book return by instance ID"""
    try:
        # Extract instance ID from "Copy #id" format
        instance_id = int(message.text.strip().split('#')[1])
        
        # Check if the instance exists and is currently borrowed
        borrowing = await borrowings_repo.get_borrowing_by_instance(db, instance_id)
        
        if not borrowing:
            await message.answer("❌ This book is not currently borrowed. Return process failed.")
            await state.clear()
            return
            
        if borrowing['user_id'] != message.from_user.id:
            await message.answer("❌ You don't borrow this book. Return process failed.")
            await state.clear()
            return
        if borrowing['state'] == 'pending':
            await message.answer("❌ This book is already pending. Return process failed.")
            await state.clear()
            return
            
        # Update borrowing state to returned
        await borrowings_repo.update_borrowing_state(db, borrowing['borrow_id'], 'pending')

        success_message = (
            f"✅ Successfully returned\n\n"
            f"📚 {borrowing['title']}\n"
            f"👤 Author: {borrowing.get('author', 'Unknown')}\n"
            f"📖 Copy #{instance_id}\n\n"
            f"Thank you for returning the book! We will check it and approve the return soon."
        )
        
        await message.answer(success_message)
        await state.clear()
        
    except (ValueError, IndexError):
        await message.answer("❌ Please select a book from the keyboard or enter a valid instance ID (number).")
    except Exception as e:
        logging.error(f"Error in process_return_book: {e}")
        await message.answer("❌ An error occurred while processing the return. Please try again.")
        await state.clear()

@dp.message(Command("borrow"))
async def command_borrow_handler(message: Message, state: FSMContext) -> None:
    """Handle /borrow command"""
    # Check if user has reached borrowing limit
    borrowings = await borrowings_repo.get_user_borrowings(db, message.from_user.id)
    if len(borrowings) >= 3:
        await message.answer("❌ You have reached the maximum number of borrowings (3)")
        return

    await message.answer(
        "📚 Please enter the instance ID of the book you want to borrow.\n"
        "You can find the instance ID on the book cover"
    )
    await state.set_state(BorrowState.SELECT_INSTANCE)

@dp.message(BorrowState.SELECT_INSTANCE)
async def process_instance_selection(message: Message, state: FSMContext) -> None:
    """Process instance selection for borrowing"""
    try:
        instance_id = int(message.text.strip())
        
        # Get instance details
        instance = await books_repo.get_instance_by_id(db, instance_id)
        if not instance:
            await message.answer("❌ Instance not found")
            await state.clear()
            return
            
        if not instance['available']:
            await message.answer("❌ This copy is not available")
            await state.clear()
            return
            
        # Get book details
        book = await books_repo.get_book_by_id(db, instance['book_id'])
        if not book:
            await message.answer("❌ Book not found")
            await state.clear()
            return
        
        # Create borrowing record
        borrow_id = await borrowings_repo.create_borrowing(db, message.from_user.id, instance_id)
        
        # Update instance availability
        await books_repo.update_book_availability(db, instance_id, False)
        
        # Get borrowing details
        borrowing = await borrowings_repo.get_borrowing_by_instance(db, instance_id)
        return_time = borrowing['borrow_return_time'].strftime('%d %b %Y')
        
        success_message = (
            f"✅ Successfully borrowed\n\n"
            f"📚 {book['title']}\n"
            f"👤 Author: {book.get('author', 'Unknown')}\n"
            f"📖 Copy #{instance_id}\n"
            f"📅 Return by: {return_time}\n\n"
            f"Back to library /books"
        )
        
        await message.answer(
            success_message,
        )
        await state.clear()
        
    except ValueError:
        await message.answer("❌ Please enter a valid instance ID (number).")
    except Exception as e:
        logging.error(f"Error in process_instance_selection: {e}")
        await message.answer("❌ An error occurred while booking the copy. Please try again.")
        await state.clear()

@dp.message(Command("refresh_books"))   
async def command_refresh_books_handler(message: Message) -> None:
    user = await user_repo.get_user(message.from_user.id)
    if user['role'] != 'admin':
        await message.answer("You are not authorized to use this command.")
    else:
        await get_books(force_refresh=True)
        await message.answer("Books refreshed")

@dp.message(Command("check"))
async def command_check_handler(message: Message) -> None:
    """Handle /check command"""
    user = await user_repo.get_user(message.from_user.id)
    if user['role'] != 'admin':
        await message.answer("You are not authorized to use this command.")
    else:
        await message.answer("🔍 Checking...")
        pending_borrowings = await get_pending_borrowings()

        if not pending_borrowings:
            await message.answer("No pending borrowings")
            return
    
        await message.answer(
            f"📚 List of pending borrowings (Page 1):",
            reply_markup=create_pending_borrowings_keyboard(pending_borrowings, 0)
        )

@dp.message(Command("open"))
async def command_open_handler(message: Message) -> None:
    """Handle /open command"""
    await message.answer("In the future, this comand will notify us that we need to open the Startup Sauna door.")


async def get_pending_borrowings(force_refresh: bool = False):
    global pending_borrowings
    if not pending_borrowings or force_refresh:
        pending_borrowings = await borrowings_repo.get_pending_borrowings(db)
    return pending_borrowings

@dp.callback_query(F.data.startswith("pending_page_"))
async def pending_page_handler(callback: CallbackQuery) -> None:
    """Handle pending borrowings pagination"""
    try:
        page = int(callback.data.split("_")[2])

        pending_borrowings = await get_pending_borrowings()
        
        
        if not pending_borrowings:
            await callback.answer("No pending borrowings", show_alert=True)
            return
            
        await callback.message.edit_text(
            f"📚 List of pending borrowings (Page {page + 1}):",
            reply_markup=create_pending_borrowings_keyboard(pending_borrowings, page)
        )
            
    except Exception as e:
        logging.error(f"Error in pending_page_handler: {e}")
        await callback.answer("An error occurred while changing pages", show_alert=True)

@dp.callback_query(F.data.startswith("pending_borrowing_"))
async def pending_borrowing_handler(callback: CallbackQuery) -> None:
    """Handle pending borrowing button clicks"""

    borrowing_id = int(callback.data.split("_")[2])  # Convert to integer
    page = int(callback.data.split("_")[3])
    borrowing = await borrowings_repo.get_borrowing_by_id(db, borrowing_id)
    text = f"📚 {borrowing['title']}\n"
    text += f"👤 Author: {borrowing['author']}\n"
    text += f"📖 Copy #{borrowing['instance_id']}\n"
    text += f"📅 Returned at: {borrowing['borrow_return_time']}\n"
    text += f"Borrowed by: @{borrowing['username']}\n"

    await callback.message.edit_text(text, reply_markup= create_approve_borrowing_keyboard(borrowing_id, page))


@dp.callback_query(F.data.startswith("state_borrowing_"))
async def state_borrowing_handler(callback: CallbackQuery, bot: Bot) -> None:
    """Handle borrowing state button clicks"""
    borrowing_id = int(callback.data.split("_")[2])  # Convert to integer
    state = callback.data.split("_")[3]
    borrowing = await borrowings_repo.get_borrowing_by_id(db, borrowing_id)
    
    if state == "1":
        await borrowings_repo.update_borrowing_state(db, borrowing_id, 'returned')
        await books_repo.update_book_availability(db, borrowing['instance_id'], True)
        await bot.send_message(borrowing['user_id'], f"Admin has approved your return for Copy #{borrowing['instance_id']}")
    elif state == "0":
        if borrowing['borrow_return_time'] < datetime.now():
            await borrowings_repo.update_borrowing_state(db, borrowing_id, 'overdue')
        else:
            await borrowings_repo.update_borrowing_state(db, borrowing_id, 'borrowed')
        await bot.send_message(borrowing['user_id'], f"Admin hasn't approved your borrowing for Copy #{borrowing['instance_id']}")
    
    pending_borrowings = await get_pending_borrowings(force_refresh=True)
    if pending_borrowings:
        await callback.message.edit_text(
            f"📚 List of pending borrowings (Page 1):",
            reply_markup=create_pending_borrowings_keyboard(pending_borrowings, 0)
        )
    else:
        await callback.message.edit_text("No pending borrowings")

@dp.message(Command("about"))
async def command_about_handler(message: Message) -> None:
    """Handle /about command"""
    about_message = (
        "🤖 *Aaltoes Library Bot*\n\n"
        "A Telegram bot for managing the Aaltoes library. "
        "Borrow and return books, check your borrowings, and stay updated with upcoming events.\n\n"
        "📚 *Features:*\n"
        "- Browse and borrow books\n"
        "- Manage your borrowings\n"
        "- Get event reminders\n"
        "- Easy book returns\n\n"
        "Type /help to see all available commands!"
    )
    
    await message.answer(about_message, parse_mode=ParseMode.MARKDOWN)

async def main() -> None:
    
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    # Connect to the database
    await db.connect(settings.DATABASE_URL_UNPOOLED)
    # Initialize tables
    await user_repo.init(db)
    await reminders_repo.init(db)
    await books_repo.init(db)
    await borrowings_repo.init(db)
    
    # Start periodic events refresh
    asyncio.create_task(periodic_events_refresh())
    
    # Start reminders checker
    asyncio.create_task(check_reminders(bot))
    asyncio.create_task(update_overdue_borrowings(bot))
    asyncio.create_task(send_overdue_notification(bot))
    
    # And the run events dispatching
    try:
        await dp.start_polling(bot)
    finally:
        # Close the database connection when the bot is stopped
        await db.close()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())