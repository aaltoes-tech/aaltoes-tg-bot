import asyncio
import logging
import sys
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from settings import settings
from db import db
from repository.books import BooksRepository

async def preload_book_images() -> None:
    """Preload all book images to Telegram and cache their file IDs"""
    # Initialize bot
    bot = Bot(token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    books_repo = BooksRepository()
    
    try:
        # Connect to database
        await db.connect(settings.DATABASE_URL_UNPOOLED)
        
        # Initialize tables
        await books_repo.init(db)
        
        # Get all instances
        instances = await books_repo.get_all_instances(db)
        if not instances:
            logging.warning("No instances found to preload images")
            return
        for instance in instances:
            if instance.get('image'):
                image_path = instance['image']
                if image_path.startswith('https://'):
                    try:    
                        # Send the image to Telegram to get its file_id
                        sent_message = await bot.send_photo(
                            chat_id=settings.ADMINS[0],  # Send to first admin
                            photo=image_path
                        )
                        
                        # Store the file_id in database
                        await books_repo.save_file_id(
                            db,
                            instance['instance_id'],
                            sent_message.photo[-1].file_id
                        )
                        
                        # Delete the message
                        await bot.delete_message(
                            chat_id=settings.ADMINS[0],
                            message_id=sent_message.message_id
                        )
                        
                        logging.info(f"Preloaded image for book {instance['instance_id']}")
                        
                    except Exception as e:
                        logging.error(f"Error preloading image for book {instance['instance_id']}: {e}")
        
        logging.info("Finished preloading images")
        
    except Exception as e:
        logging.error(f"Error in preload_book_images: {e}")
    finally:
        # Close database connection
        await db.close()
        # Close bot session
        await bot.session.close()

if __name__ == "__main__":
    
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(preload_book_images()) 