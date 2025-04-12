import asyncio
import logging
import sys
from settings import settings
from db import db
from repository.books import BooksRepository

async def main():
    # Initialize books repository
    books_repo = BooksRepository()
    
    # Connect to database
    await db.connect(settings.DATABASE_URL_UNPOOLED)
    
    try:
        # Clear existing books
        await db.execute("TRUNCATE TABLE books RESTART IDENTITY")
        logging.info("Cleared existing books from database")
        
        # Initialize books table
        await books_repo.init(db)
        
        # Upload books from CSV
        await books_repo.upload_books_from_csv(db, "books.csv")
        
        # Verify books were loaded
        books = await books_repo.get_all_books(db)
        logging.info(f"Loaded {len(books)} books into the database")
        
    except Exception as e:
        logging.error(f"Error loading books: {e}")
    finally:
        # Close database connection
        await db.close()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main()) 