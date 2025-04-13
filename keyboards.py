from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from typing import Dict, List, Any
from datetime import datetime
import pytz
import logging

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
        
        # Format time with timezone abbreviation
        tz_abbr = local_time.strftime('%Z')
        return f"{local_time.strftime('%d %b %Y, %H:%M')}"
    except Exception as e:
        logging.error(f"Error formatting event time: {e}")
        # Fallback to simple formatting if there's an error
        return event['start_time'].strftime('%d %b %Y, %H:%M')

def create_events_keyboard(events: Dict[str, Dict]) -> InlineKeyboardMarkup:
    """Create keyboard with event buttons"""
    keyboard = []
    for event_id, event in events.items():
        keyboard.append([InlineKeyboardButton(
            text=event['title'],
            callback_data=f"event_{event_id}"
        )])
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def create_back_to_events_keyboard() -> InlineKeyboardMarkup:
    """Create keyboard with back button"""
    keyboard = [[InlineKeyboardButton(
        text="⬅️ Back to Events",
        callback_data="back_to_events"
    )]]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def create_event_details_keyboard(event_id: str, has_reminder: bool = False) -> InlineKeyboardMarkup:
    """Create keyboard with event details buttons"""
    keyboard = []
    
    if has_reminder:
        keyboard.append([InlineKeyboardButton(
            text="❌ Remove Reminder",
            callback_data=f"remove_reminder_{event_id}"
        )])
    else:
        keyboard.append([InlineKeyboardButton(
            text="🔔 Set Reminder",
            callback_data=f"reminder_{event_id}"
        )])
    
    keyboard.append([InlineKeyboardButton(
        text="⬅️ Back to Events",
        callback_data="back_to_events"
    )])
    
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def get_availability_emoji(occupied: int, total: int) -> str:
    """Get the appropriate emoji based on availability"""
    return "✅" if occupied < total else "❌"

def create_books_keyboard(books: List[Dict], page: int = 0, books_per_page: int = 5) -> InlineKeyboardMarkup:
    """Create keyboard with paginated book buttons"""
    keyboard = []
    
    # Calculate start and end indices for current page
    start_idx = page * books_per_page
    end_idx = min(start_idx + books_per_page, len(books))
    
    # Add book buttons for current page
    for book in books[start_idx:end_idx]:
        # Get availability info from pre-processed book data
        counts = book['availability']
        availability_emoji = get_availability_emoji(counts['occupied'], counts['total'])
        keyboard.append([InlineKeyboardButton(
            text=f"{availability_emoji} ({counts['occupied']}/{counts['total']})  {book['title']}",
            callback_data=f"book_{book['book_id']}_{page}"
        )])
    
    # Add navigation buttons
    navigation_buttons = []
    
    # Add previous page button if not on first page
    if page > 0:
        navigation_buttons.append(InlineKeyboardButton(
            text="⬅️ Previous",
            callback_data=f"books_page_{page-1}"
        ))
    
    # Add next page button if there are more books
    if end_idx < len(books):
        navigation_buttons.append(InlineKeyboardButton(
            text="Next ➡️",
            callback_data=f"books_page_{page+1}"
        ))
    
    if navigation_buttons:
        keyboard.append(navigation_buttons)
    
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def create_book_details_keyboard(book_id: int, current_page: int = 0) -> InlineKeyboardMarkup:
    """Create keyboard with book details buttons"""
    keyboard = [[InlineKeyboardButton(
        text="⬅️ Back to Books",
        callback_data=f"back_to_books_{current_page}"
    )]]
    return InlineKeyboardMarkup(inline_keyboard=keyboard) 