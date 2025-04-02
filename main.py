import asyncio
import logging
import sys
from datetime import datetime, timedelta
from typing import Dict, List, Tuple, Any

import pytz
from timezonefinder import TimezoneFinder

from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters.command import Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from settings import settings
from db import db
from repository.user import UserRepository
from repository.events import EventsRepository
from repository.reminders import RemindersRepository
from keyboards import create_events_keyboard, create_back_to_events_keyboard, create_event_details_keyboard

# Initialize timezone finder
tf = TimezoneFinder()
ADMINS = [
    '658415666', '468596234'
]
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

# Initialize storage
storage = MemoryStorage()

# Initialize dispatcher
dp = Dispatcher(storage=storage)

# Store events data in memory with timestamp
current_events: Dict[str, Dict] = {}
last_events_update: datetime = None
EVENTS_CACHE_DURATION = timedelta(hours=1)  # Cache events for 1 hour

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

async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    
    # Connect to the database
    await db.connect(settings.DATABASE_URL)
    
    # Initialize tables
    await user_repo.init(db)
    await reminders_repo.init(db)
    
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