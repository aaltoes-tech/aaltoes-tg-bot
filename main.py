import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from settings import settings
from db import db
from repository.user import UserRepository

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()
user_repo = UserRepository()


@dp.message(CommandStart())
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
    
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


@dp.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    
    # Connect to the database
    await db.connect(settings.DATABASE_URL)
    
    # Initialize user table
    await user_repo.init(db)
    
    # And the run events dispatching
    try:
        await dp.start_polling(bot)
    finally:
        # Close the database connection when the bot is stopped
        await db.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())