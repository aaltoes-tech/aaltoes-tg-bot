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
        self.instances_table_name = "books_instances"
    
    async def init(self, db) -> None:
        """Initialize books and books_instances tables"""
        try:
            # Create books table
            await db.execute(f"""
                CREATE TABLE IF NOT EXISTS {self.table_name} (
                    book_id SERIAL PRIMARY KEY,
                    title TEXT NOT NULL,
                    author TEXT,
                    year INTEGER,
                    description TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Create books_instances table
            await db.execute(f"""
                CREATE TABLE IF NOT EXISTS {self.instances_table_name} (
                    instance_id SERIAL PRIMARY KEY,
                    book_id INTEGER REFERENCES {self.table_name}(book_id),
                    image TEXT NOT NULL,
                    available BOOLEAN DEFAULT TRUE,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            logging.info(f"Tables {self.table_name} and {self.instances_table_name} initialized successfully")
        except Exception as e:
            logging.error(f"Error initializing tables: {e}")
            raise

    async def get_all_books(self, db) -> List[Dict]:
        """Get all books with their instance counts"""
        try:
            query = f"""
                SELECT 
                    b.book_id,
                    b.title,
                    b.author,
                    b.year,
                    b.description,
                    b.created_at,
                    (
                        SELECT COUNT(*) 
                        FROM {self.instances_table_name} bi 
                        WHERE bi.book_id = b.book_id
                    ) as total_instances,
                    (
                        SELECT COUNT(*) 
                        FROM {self.instances_table_name} bi 
                        WHERE bi.book_id = b.book_id AND bi.available = TRUE
                    ) as available_instances,
                    (
                        SELECT image 
                        FROM {self.instances_table_name} bi 
                        WHERE bi.book_id = b.book_id AND bi.available = TRUE 
                        LIMIT 1
                    ) as image
                FROM {self.table_name} b
                ORDER BY b.title
            """
            results = await db.fetch(query)
            logging.info(f"Database query returned {len(results)} results")
            
            # Convert results to dictionaries
            books = []
            for row in results:
                try:
                    # Log the row to see its structure
                    logging.info(f"Processing row: {row}")
                    
                    # Check if row is a dictionary or tuple
                    if isinstance(row, dict):
                        book = row
                    else:
                        # Handle tuple/array result
                        book = {
                            'book_id': row[0],
                            'title': row[1],
                            'author': row[2],
                            'year': row[3],
                            'description': row[4],
                            'created_at': row[5],
                            'total_instances': row[6],
                            'available_instances': row[7],
                            'image': row[8]
                        }
                    books.append(book)
                except Exception as e:
                    logging.error(f"Error processing row {row}: {e}")
                    continue
            
            logging.info(f"Successfully processed {len(books)} books")
            return books
        except Exception as e:
            logging.error(f"Error getting all books: {e}")
            return []

    async def get_book_by_id(self, db, book_id: int) -> Dict:
        """Get a book by ID with its instance counts"""
        try:
            query = f"""
                SELECT b.*, 
                       COUNT(bi.instance_id) as total_instances,
                       COUNT(CASE WHEN bi.available = TRUE THEN 1 END) as available_instances
                FROM {self.table_name} b
                LEFT JOIN {self.instances_table_name} bi ON b.book_id = bi.book_id
                WHERE b.book_id = $1
                GROUP BY b.book_id
            """
            result = await db.execute(query, book_id)
            return result[0] if result else None
        except Exception as e:
            logging.error(f"Error getting book by ID: {e}")
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

            # Insert book and get the book_id
            result = await db.execute(f"""
                INSERT INTO {self.table_name} (title, author, year, description)
                VALUES ($1, $2, $3, $4)
                RETURNING book_id
            """, title, author, year, description)
            
            book_id = result[0]['book_id']

            # Handle image path for instance
            if 'image' in book_data and not pd.isna(book_data['image']):
                image = str(book_data['image']).strip()
                if image:
                    # Convert to absolute path
                    image = os.path.abspath(os.path.join('books/books_images', image))
                    # Check if file exists
                    if not os.path.exists(image):
                        logging.warning(f"Image file not found: {image}")
                        image = None
                    
                    if image:
                        # Insert instance with image
                        await db.execute(f"""
                            INSERT INTO {self.instances_table_name} (book_id, image)
                            VALUES ($1, $2)
                        """, book_id, image)
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
            return await db.execute(f"""
                SELECT * FROM {self.table_name}
                WHERE title ILIKE $1 OR author ILIKE $1
                ORDER BY title
            """, f"%{query}%")
        except Exception as e:
            logging.error(f"Error searching books: {e}")
            return []

    async def get_book_instances(self, db, book_id: int) -> List[Dict]:
        """Get all instances of a book with their availability status"""
        try:
            query = f"""
                SELECT 
                    instance_id,
                    image,
                    available,
                    created_at
                FROM {self.instances_table_name}
                WHERE book_id = $1
                ORDER BY instance_id
            """
            results = await db.fetch(query, book_id)
            logging.info(f"Database query returned {len(results)} instances for book {book_id}")
            
            # Convert results to dictionaries
            instances = []
            for row in results:
                try:
                    # Check if row is a dictionary or tuple
                    if isinstance(row, dict):
                        instance = row
                    else:
                        # Handle tuple/array result
                        instance = {
                            'instance_id': row[0],
                            'image': row[1],
                            'available': row[2],
                            'created_at': row[3]
                        }
                    instances.append(instance)
                except Exception as e:
                    logging.error(f"Error processing instance row {row}: {e}")
                    continue
            
            return instances
        except Exception as e:
            logging.error(f"Error getting book instances: {e}")
            return []

    async def update_book_availability(self, db, instance_id: int, available: bool) -> None:
        """Update availability status of a book instance"""
        try:
            await db.execute(f"""
                UPDATE {self.instances_table_name}
                SET available = $1
                WHERE instance_id = $2
            """, available, instance_id)
        except Exception as e:
            logging.error(f"Error updating book availability: {e}")

    async def upload_books_from_csv(self, db, csv_path="books.csv", instances_csv_path="books_instances.csv"):
        """Upload books from CSV files to database"""
        try:
            # Read books CSV file
            books_df = pd.read_csv(csv_path)
            
            # Insert books
            for _, row in books_df.iterrows():
                # Handle author field which can be NaN
                author = None
                if not pd.isna(row['author']):
                    author = str(row['author']).strip()
                    if not author:  # Empty string after strip
                        author = None
                
                # Handle year field which can be NaN
                year = None
                if not pd.isna(row['year']):
                    try:
                        year = int(row['year'])
                    except (ValueError, TypeError):
                        year = None
                
                # Handle description field which can be NaN
                description = None
                if not pd.isna(row['description']):
                    description = str(row['description']).strip()
                    if not description:  # Empty string after strip
                        description = None
                
                # Insert book
                await db.execute(f"""
                    INSERT INTO {self.table_name} (book_id, title, author, year, description)
                    VALUES ($1, $2, $3, $4, $5)
                """, int(row['book_id']), str(row['title']), author, year, description)
            
            # Read instances CSV file
            instances_df = pd.read_csv(instances_csv_path)
            
            # Insert instances
            for _, row in instances_df.iterrows():
                # Convert instance_id and book_id to integers
                instance_id = int(row['instance_id'])
                book_id = int(row['book_id'])
                
                # Insert instance
                await db.execute(f"""
                    INSERT INTO {self.instances_table_name} (instance_id, book_id, image)
                    VALUES ($1, $2, $3)
                """, instance_id, book_id, str(row['image']))
            
            logging.info(f"Successfully uploaded {len(books_df)} books and {len(instances_df)} instances to database")
            
        except Exception as e:
            logging.error(f"Error uploading books: {str(e)}")
            raise

async def get_books_by_author(author: str):
    """Get books by author"""
    return await db.fetch("SELECT * FROM books WHERE author = $1", author)

async def get_books_by_year(year: int):
    """Get books by publication year"""
    return await db.fetch("SELECT * FROM books WHERE year = $1", year)
