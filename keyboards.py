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

def create_books_keyboard(books: List[Dict], current_page: int = 0, books_per_page: int = 5) -> InlineKeyboardMarkup:
    """Create keyboard for books list with pagination"""
    keyboard = []
    
    # Calculate start and end indices for current page
    start_idx = current_page * books_per_page
    end_idx = min(start_idx + books_per_page, len(books))  # Ensure we don't go past the end
    page_books = books[start_idx:end_idx]
    
    logging.info(f"Creating keyboard for page {current_page} (books {start_idx} to {end_idx} of {len(books)})")
    
    # Add book buttons
    for book in page_books:
        # Get availability info
        total_instances = book.get('total_instances', 0)
        available_instances = book.get('available_instances', 0)
        
        # Create button text with availability
        button_text = f"{get_availability_emoji(total_instances - available_instances, total_instances)} ({available_instances}/{total_instances}) {book.get('title', 'No title')}"
        keyboard.append([InlineKeyboardButton(
            text=button_text,
            callback_data=f"book_{book['book_id']}_{current_page}"
        )])
    
    # Add navigation buttons
    navigation_buttons = []
    
    # Add previous page button if not on first page
    if current_page > 0:
        navigation_buttons.append(InlineKeyboardButton(
            text="⬅️ Previous",
            callback_data=f"books_page_{current_page - 1}"
        ))
    
    # Add next page button if there are more books
    if end_idx < len(books):
        navigation_buttons.append(InlineKeyboardButton(
            text="Next ➡️",
            callback_data=f"books_page_{current_page + 1}"
        ))
    
    if navigation_buttons:
        keyboard.append(navigation_buttons)
    
    logging.info(f"Created keyboard with {len(page_books)} books and {len(navigation_buttons)} navigation buttons")
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def create_book_details_keyboard(book_id: int, current_page: int, available_instances: int) -> InlineKeyboardMarkup:
    """Create keyboard for book details with back button and book button if available"""
    keyboard = []
    
    if available_instances > 0:
        keyboard.append([
            InlineKeyboardButton(
                text="📚 Borrow a Copy",
                callback_data=f"book_instance_select_{book_id}"
            )
        ])
    
    # Add Back to Books button
    keyboard.append([
        InlineKeyboardButton(
            text="⬅️ Back to Books",
            callback_data=f"return_to_books_{current_page}"
        )
    ])
    
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def create_instance_selection_keyboard(instances: List[Dict], book_id: int) -> InlineKeyboardMarkup:
    """Create keyboard for instance selection"""
    keyboard = []
    for instance in instances:
        if instance['available']:
            keyboard.append([InlineKeyboardButton(
                text=f"Copy #{instance['instance_id']}",
                callback_data=f"book_instance_{instance['instance_id']}_{book_id}"
            )])
    
    # Add Back button
    keyboard.append([InlineKeyboardButton(
        text="Back to Book Details",
        callback_data=f"back_to_book_{book_id}"
    )])
    
    return InlineKeyboardMarkup(inline_keyboard=keyboard) 