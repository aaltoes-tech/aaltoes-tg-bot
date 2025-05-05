from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
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
            text=f"{format_event_time(event)} – {event['title']}",
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
                callback_data=f"instance_select_{book_id}_{current_page}"
            )
        ])
    
    # Add Back to Books button
    keyboard.append([
        InlineKeyboardButton(
            text="⬅️ Back to Books",
            callback_data=f"books_page_{current_page}"
        )
    ])
    
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def create_instance_selection_keyboard(instances: List[Dict], book_id: int, current_page: int) -> InlineKeyboardMarkup:
    """Create keyboard for instance selection"""
    keyboard = []
    for instance in instances:
        if instance['available']:
            keyboard.append([InlineKeyboardButton(
                text=f"Copy #{instance['instance_id']}",
                callback_data=f"instance_{instance['instance_id']}_{book_id}"
            )])

        # Add back button
    keyboard.append([
        InlineKeyboardButton(
            text="⬅️ Back to Book",
            callback_data=f"book_{book_id}_{current_page}"  # Added page number for back navigation
        )
    ])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def create_pending_borrowings_keyboard(pending_borrowings: List[Dict], page: int = 0) -> InlineKeyboardMarkup:
    """Create keyboard for pending borrowings with pagination"""
    keyboard = []
    items_per_page = 5
    start_idx = page * items_per_page
    end_idx = start_idx + items_per_page
    current_page_borrowings = pending_borrowings[start_idx:end_idx]
    
    # Add borrowings for current page
    for borrowing in current_page_borrowings:
        keyboard.append([
            InlineKeyboardButton(
                text=f"Copy #{borrowing['instance_id']} - {borrowing['title']}",
                callback_data=f"pending_borrowing_{borrowing['borrow_id']}_{page}"
            )
        ])
    
    # Add pagination buttons
    total_pages = (len(pending_borrowings) + items_per_page - 1) // items_per_page
    pagination_buttons = []
    
    if page > 0:
        pagination_buttons.append(
            InlineKeyboardButton(
                text="⬅️ Previous",
                callback_data=f"pending_page_{page-1}"
            )
        )
    
    if page < total_pages - 1:
        pagination_buttons.append(
            InlineKeyboardButton(
                text="Next ➡️",
                callback_data=f"pending_page_{page+1}"
            )
        )
    
    if pagination_buttons:
        keyboard.append(pagination_buttons)
    
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def create_approve_borrowing_keyboard(borrowing_id: str, page: int) -> InlineKeyboardMarkup:
    """Create keyboard for approving borrowing"""
    keyboard = []
    keyboard.append([
        InlineKeyboardButton(text="Approve", callback_data=f"state_borrowing_{borrowing_id}_1"),
        InlineKeyboardButton(text="Decline", callback_data=f"state_borrowing_{borrowing_id}_0")
    ])

    keyboard.append([InlineKeyboardButton(text="Back", callback_data=f"pending_page_{page}")])
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def create_return_keyboard(borrowings: List[Dict]) -> ReplyKeyboardMarkup:
    """Create keyboard for returning a book"""
    keyboard = []
    for borrowing in borrowings:
        keyboard.append([KeyboardButton(
            text=f"Copy #{borrowing['instance_id']}"
        )])
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True, one_time_keyboard=True)

def create_apply_keyboard() -> InlineKeyboardMarkup:
    """Create keyboard for applying for access"""
    keyboard = []
    keyboard.append([
        InlineKeyboardButton(text="Apply", callback_data=f"apply"),
    ])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def create_confirm_keyboard() -> ReplyKeyboardMarkup:
    """Create keyboard for confirming application"""
    keyboard = [
        [KeyboardButton(text="Confirm"), 
         KeyboardButton(text="Cancel")]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True, one_time_keyboard=True)

def create_requests_keyboard(requests: List[Dict], page: int = 0) -> InlineKeyboardMarkup:
    """Create keyboard for requests with pagination"""
    keyboard = []
    requests_per_page = 5
    start_idx = page * requests_per_page
    end_idx = start_idx + requests_per_page
    current_page_requests = requests[start_idx:end_idx]
    
    # Add request buttons
    for request in current_page_requests:
        request_text = f"Request ID: {request['request_id']}\n"
        keyboard.append([InlineKeyboardButton(text=request_text, callback_data=f"request_{request['request_id']}_{page}")])
    
    # Add pagination buttons
    pagination_buttons = []
    if page > 0:
        pagination_buttons.append(InlineKeyboardButton(text="⬅️ Previous", callback_data=f"requests_page_{page-1}"))
    if end_idx < len(requests):
        pagination_buttons.append(InlineKeyboardButton(text="Next ➡️", callback_data=f"requests_page_{page+1}"))
    
    if pagination_buttons:
        keyboard.append(pagination_buttons)
    
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def create_approve_request_keyboard(request_id: int, page: int) -> InlineKeyboardMarkup:
    """Create keyboard for approving a request"""
    keyboard = []
    keyboard.append([InlineKeyboardButton(text="Approve", callback_data=f"change_request_state_{request_id}_1"),
                    InlineKeyboardButton(text="Reject", callback_data=f"change_request_state_{request_id}_0")])
    keyboard.append([InlineKeyboardButton(text="Back", callback_data=f"requests_page_{page}")])
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def create_users_keyboard(users: List[Dict], page: int = 0) -> InlineKeyboardMarkup:
    """Create keyboard for users with pagination"""
    keyboard = []
    users_per_page = 5
    start_idx = page * users_per_page
    end_idx = start_idx + users_per_page
    current_page_users = users[start_idx:end_idx]
    
    # Add user buttons
    for user in current_page_users:
        keyboard.append([InlineKeyboardButton(text=f"{user['name']} - @{user['username']}", callback_data=f"user_{user['user_id']}_{page}")])
    
    # Add pagination buttons
    pagination_buttons = []
    if page > 0:
        pagination_buttons.append(InlineKeyboardButton(text="⬅️ Previous", callback_data=f"users_page_{page-1}"))
    if end_idx < len(users):
        pagination_buttons.append(InlineKeyboardButton(text="Next ➡️", callback_data=f"users_page_{page+1}"))
    
    if pagination_buttons:
        keyboard.append(pagination_buttons)
    
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def create_update_user_keyboard(user: Dict, page: int) -> InlineKeyboardMarkup:
    """Create keyboard for updating a user"""
    keyboard = []
    keyboard.append([InlineKeyboardButton(text="Suspend access", callback_data=f"suspend_access_{user['id']}")])
    keyboard.append([InlineKeyboardButton(text="Back", callback_data=f"users_page_{page}")])
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def create_actions_keyboard(page: int = 0) -> InlineKeyboardMarkup:
    """Create keyboard for actions with specific page layout"""
    # Define pages with their specific actions
    pages = [
        [  # Page 1
            ("🚪 Open Startup Sauna", "action_open_sauna"),
            ("❓ Show Commands", "action_help"),
            ("✏️ Update Profile Name", "action_change_name"),
            ("📅 View Events", "action_events")
        ],
        [  # Page 2
            ("📝 Apply for Access Card", "action_apply"),
            ("🔑 Check Access Card Status", "action_access"),
            ("✅ Verify Account", "action_confirm"),
            ("🔔 My Reminders", "action_reminders")
        ],
        [  # Page 3
            ("📚 My Books", "action_borrowings"),
            ("📖 Get Book", "action_borrow"),
            ("↩️ Return Book", "action_return"),
            ("📋 Past Loans", "action_history")
        ]
    ]
    
    # Create keyboard
    keyboard = []
    
    # Add action buttons for current page
    for text, callback_data in pages[page]:
        keyboard.append([InlineKeyboardButton(text=text, callback_data=callback_data)])
    
    # Add pagination buttons
    pagination_buttons = []
    if page > 0:
        pagination_buttons.append(InlineKeyboardButton(text="⬅️ Previous", callback_data=f"actions_page_{page-1}"))
    if page < len(pages) - 1:
        pagination_buttons.append(InlineKeyboardButton(text="Next ➡️", callback_data=f"actions_page_{page+1}"))
    
    if pagination_buttons:
        keyboard.append(pagination_buttons)
    
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

