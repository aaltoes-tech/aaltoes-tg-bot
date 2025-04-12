import pandas as pd
import os
from dotenv import load_dotenv
from db import db
import logging
from typing import List, Dict, Optional
from datetime import datetime

# Load environment variables
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

class BooksRepository:
    def __init__(self):
        self.table_name = "books"
    
    async def init(self, db) -> None:
        """Initialize the books table"""
        try:
            await db.execute(f"""
                CREATE TABLE IF NOT EXISTS {self.table_name} (
                    id SERIAL PRIMARY KEY,
                    book_id INTEGER UNIQUE NOT NULL,
                    author VARCHAR(255),
                    year INTEGER,
                    title VARCHAR(255),
                    description TEXT,
                    image VARCHAR(255) NOT NULL,
                    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
                )
            """)
            logging.info("Books table initialized successfully")
        except Exception as e:
            logging.error(f"Error initializing books table: {e}")

    async def get_all_books(self, db) -> List[Dict]:
        """Get all books from the database"""
        try:
            return await db.fetch(f"SELECT * FROM {self.table_name} ORDER BY title")
        except Exception as e:
            logging.error(f"Error fetching all books: {e}")
            return []

    async def get_book_by_id(self, db, book_id: int) -> Optional[Dict]:
        """Get a book by its ID"""
        try:
            return await db.fetchrow(f"SELECT * FROM {self.table_name} WHERE book_id = $1", book_id)
        except Exception as e:
            logging.error(f"Error fetching book by ID: {e}")
            return None

    async def save_book(self, db, book_data: Dict) -> None:
        """Save a book to the database"""
        try:
            # Handle all fields as optional with proper type conversion
            book_id = None
            if 'book_id' in book_data and not pd.isna(book_data['book_id']):
                try:
                    book_id = int(book_data['book_id'])
                except (ValueError, TypeError):
                    book_id = None

            author = None
            if 'author' in book_data and not pd.isna(book_data['author']):
                author = str(book_data['author']).strip()
                if not author:  # Empty string after strip
                    author = None

            year = None
            if 'year' in book_data and not pd.isna(book_data['year']):
                try:
                    year = int(book_data['year'])
                except (ValueError, TypeError):
                    year = None

            title = None
            if 'title' in book_data and not pd.isna(book_data['title']):
                title = str(book_data['title']).strip()
                if not title:  # Empty string after strip
                    title = None

            description = None
            if 'description' in book_data and not pd.isna(book_data['description']):
                description = str(book_data['description']).strip()
                if not description:  # Empty string after strip
                    description = None

            # Handle image path
            image = None
            if 'image' in book_data and not pd.isna(book_data['image']):
                image = str(book_data['image']).strip()
                if image:
                    # Convert to absolute path
                    image = os.path.abspath(os.path.join('books/books_images', image))
                    # Check if file exists
                    if not os.path.exists(image):
                        logging.warning(f"Image file not found: {image}")
                        image = None

            await db.execute(f"""
                INSERT INTO {self.table_name} (book_id, author, year, title, description, image)
                VALUES ($1, $2, $3, $4, $5, $6)
                ON CONFLICT (book_id) DO NOTHING
            """, book_id, author, year, title, description, image)
        except Exception as e:
            logging.error(f"Error saving book: {e}")
            logging.error(f"Book data: {book_data}")

    async def delete_book(self, db, book_id: int) -> None:
        """Delete a book from the database"""
        try:
            await db.execute(f"DELETE FROM {self.table_name} WHERE book_id = $1", book_id)
        except Exception as e:
            logging.error(f"Error deleting book: {e}")

    async def search_books(self, db, query: str) -> List[Dict]:
        """Search books by title or author"""
        try:
            return await db.fetch(f"""
                SELECT * FROM {self.table_name}
                WHERE title ILIKE $1 OR author ILIKE $1
                ORDER BY title
            """, f"%{query}%")
        except Exception as e:
            logging.error(f"Error searching books: {e}")
            return []

    async def get_books_by_author(self, db, author: str) -> List[Dict]:
        """Get books by author"""
        try:
            return await db.fetch(f"SELECT * FROM {self.table_name} WHERE author = $1", author)
        except Exception as e:
            logging.error(f"Error fetching books by author: {e}")
            return []

    async def get_books_by_year(self, db, year: int) -> List[Dict]:
        """Get books by publication year"""
        try:
            return await db.fetch(f"SELECT * FROM {self.table_name} WHERE year = $1", year)
        except Exception as e:
            logging.error(f"Error fetching books by year: {e}")
            return []

    async def upload_books_from_csv(self, db, csv_path="books/books.csv"):
        """Upload books from CSV file to database"""
        try:
            # Read CSV file
            df = pd.read_csv(csv_path)
            
            # Convert year to integer, handling NaN values
            df['year'] = pd.to_numeric(df['year'], errors='coerce').astype('Int64')
            
            # Convert image paths to absolute paths
            if 'image' in df.columns:
                df['image'] = df['image'].apply(lambda x: os.path.abspath(os.path.join('images/books_images', str(x).strip())) 
                                              if not pd.isna(x) else None)
            
            # Insert records
            for _, row in df.iterrows():
                await self.save_book(db, {
                    'book_id': row['book_id'],
                    'author': row['author'],
                    'year': row['year'],
                    'title': row['title'],
                    'description': row['description'],
                    'image': row['image']
                })
            
            logging.info(f"Successfully uploaded {len(df)} books to database")
            
        except Exception as e:
            logging.error(f"Error uploading books: {str(e)}")

async def get_books_by_author(author: str):
    """Get books by author"""
    return await db.fetch("SELECT * FROM books WHERE author = $1", author)

async def get_books_by_year(year: int):
    """Get books by publication year"""
    return await db.fetch("SELECT * FROM books WHERE year = $1", year)
