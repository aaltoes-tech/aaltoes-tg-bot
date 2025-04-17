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
        # Initialize books table first
        await books_repo.init(db)
        logging.info("Initialized books tables")
        
        # Clear existing data
        await db.execute("TRUNCATE TABLE books_instances CASCADE")
        await db.execute("TRUNCATE TABLE books CASCADE")
        logging.info("Cleared existing books from database")
        
        # Upload books from CSV
        try:
            await books_repo.upload_books_from_csv(db, "books.csv", "books_instances.csv")
        except Exception as e:
            logging.error(f"Error uploading books: {e}")
            sys.exit(1)
        
        # Verify books were loaded
        books = await books_repo.get_all_books(db)
        if not books:
            logging.error("No books were loaded into the database")
            sys.exit(1)
            
        logging.info(f"Successfully loaded {len(books)} books into the database")
        
        # Verify instances were loaded
        total_instances = 0
        for book in books:
            instances = await books_repo.get_book_instances(db, book['book_id'])
            total_instances += len(instances)
            logging.info(f"Book '{book['title']}' has {len(instances)} instances")
            
        logging.info(f"Total instances loaded: {total_instances}")
        
    except Exception as e:
        logging.error(f"Error loading books: {e}")
        sys.exit(1)
    finally:
        # Close database connection
        await db.close()

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    asyncio.run(main()) 