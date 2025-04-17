# Aaltoes Telegram Bot

A Telegram bot for managing the Aaltoes library and Startup Sauna access requests.

## Features

- **Library Management**
  - Browse available books
  - Borrow and return books
  - View borrowing history
  - Get notifications for overdue books

- **Startup Sauna Access**
  - Apply for Startup Sauna access
  - Track application status
  - Receive secret access codes
  - Admin management of access requests

- **Admin Features**
  - Manage borrowings
  - Review and process access requests
  - Send notifications to users

## Setup

### Prerequisites

- Python 3.8 or higher
- PostgreSQL database
- Telegram Bot Token (from BotFather)

### Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
BOT_TOKEN=your_telegram_bot_token
DATABASE_URL_UNPOOLED=your_database_url
LUMA_API_KEY=your_luma_api_key
```

Note: Admin user IDs are configured in `settings.py` and do not need to be set in the environment variables.

### Dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```

### Required Files

1. `main.py` - Main bot application
2. `keyboards.py` - Custom keyboard layouts
3. `repository/` - Database operations
   - `books.py` - Book management
   - `borrowings.py` - Borrowing operations
   - `requests.py` - Access request management
   - `user.py` - User management
4. `db.py` - Database connection
5. `requirements.txt` - Python dependencies
6. `.env` - Environment variables

### Database Setup

1. Create a PostgreSQL database
2. The bot will automatically create the necessary tables on first run:
   - `tg_user` - User information
   - `books` - Book catalog
   - `book_instances` - Individual book copies
   - `borrowings` - Book borrowing records
   - `access_requests` - Startup Sauna access requests

### Running the Bot

1. Set up your environment variables
2. Install dependencies
3. Run the bot:

```bash
python main.py
```

## Usage

### User Commands

- `/start` - Start the bot
- `/help` - Show available commands
- `/info` - Information about Aaltoes
- `/books` - Browse available books
- `/borrow` - Borrow a book
- `/return` - Return a book
- `/borrowings` - View your borrowed books
- `/apply` - Apply for Startup Sauna access
- `/access` - Check your access status

### Admin Commands

- `/admin` - Access admin panel
- `/check` - Approval of 'return' of book request
- `/approve` - Review access requests
- `/access` - List users with access + codes, suspending if needed

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

