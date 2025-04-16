import os
from db import db
import logging
from typing import List, Dict, Optional
from datetime import datetime

class BooksRepository:
    def __init__(self):
        self.table_name = "books"
        self.instances_table_name = "books_instances"
    
    async def init(self, db) -> None:
        """Initialize books and books_instances tables"""
        try:
            logging.info("Starting table initialization...")
            
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
            logging.info(f"Created/verified {self.table_name} table")
            
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
            logging.info(f"Created/verified {self.instances_table_name} table")
            
            # Create book_image_cache table
            await db.execute(f"""
                CREATE TABLE IF NOT EXISTS instance_image_cache (
                    instance_id INTEGER PRIMARY KEY REFERENCES {self.instances_table_name}(instance_id),
                    file_id TEXT NOT NULL,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            logging.info("Created/verified instance_image_cache table")
            
            logging.info(f"All tables initialized successfully")
        except Exception as e:
            logging.error(f"Error initializing tables: {e}")
            logging.error(f"Error type: {type(e)}")
            logging.error(f"Error details: {str(e)}")
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


    async def delete_book(self, db, book_id: int) -> None:
        """Delete a book from the database"""
        try:
            await db.execute(f"DELETE FROM {self.table_name} WHERE book_id = $1", book_id)
            await db.execute(f"DELETE FROM {self.instances_table_name} WHERE book_id = $1", book_id)
        except Exception as e:
            logging.error(f"Error deleting book: {e}")
    
    async def delete_instance(self, db, instance_id: int) -> None:
        """Delete an instance from the database"""
        try:
            await db.execute(f"DELETE FROM {self.instances_table_name} WHERE instance_id = $1", instance_id)
        except Exception as e:
            logging.error(f"Error deleting instance: {e}")

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
    async def get_instance_by_id(self, db, instance_id: int) -> Dict:
        """Get an instance by ID"""
        try:
            query = """
                SELECT bi.*, b.title, b.author, b.year, b.description
                FROM book_instances bi
                JOIN books b ON bi.book_id = b.book_id
                WHERE bi.instance_id = $1
            """
            result = await db.fetchrow(query, instance_id)
            return dict(result) if result else None
        except Exception as e:
            logging.error(f"Error getting instance by ID: {e}")
            return None
    async def get_all_instances(self, db) -> List[Dict]:
        """Get all instances of all books"""
        try:
            return await db.fetch("SELECT * FROM books_instances")
        except Exception as e:
            logging.error(f"Error getting all instances: {e}")
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
            import csv
            
            # Read books CSV file
            with open(csv_path, 'r', encoding='utf-8') as f:
                books_reader = csv.DictReader(f)
                
                # Insert books
                for row in books_reader:
                    # Handle author field which can be empty
                    author = row['author'].strip() if row['author'] else None
                    
                    # Handle year field which can be empty
                    year = None
                    if row['year']:
                        try:
                            year = int(row['year'])
                        except (ValueError, TypeError):
                            year = None
                    
                    # Handle description field which can be empty
                    description = row['description'].strip() if row['description'] else None
                    
                    # Insert book
                    await db.execute(f"""
                        INSERT INTO {self.table_name} (book_id, title, author, year, description)
                        VALUES ($1, $2, $3, $4, $5)
                    """, int(row['book_id']), row['title'], author, year, description)
            
            # Read instances CSV file
            with open(instances_csv_path, 'r', encoding='utf-8') as f:
                instances_reader = csv.DictReader(f)
                
                # Insert instances
                for row in instances_reader:
                    # Convert instance_id and book_id to integers
                    instance_id = int(row['instance_id'])
                    book_id = int(row['book_id'])
                    
                    # Insert instance
                    await db.execute(f"""
                        INSERT INTO {self.instances_table_name} (instance_id, book_id, image)
                        VALUES ($1, $2, $3)
                    """, instance_id, book_id, row['image'])
            
            logging.info(f"Successfully uploaded books and instances to database")
            
        except Exception as e:
            logging.error(f"Error uploading books: {str(e)}")
            raise

    async def get_file_id(self, db, instance_id: int) -> str | None:
        """Get cached file_id for a book"""
        result = await db.fetchrow(
            "SELECT file_id FROM instance_image_cache WHERE instance_id = $1",
            instance_id
        )
        return result['file_id'] if result else None

    async def save_file_id(self, db, instance_id: int, file_id: str) -> None:
        """Save file_id for a book"""
        await db.execute(
            """
            INSERT INTO instance_image_cache (instance_id, file_id)
            VALUES ($1, $2)
            ON CONFLICT (instance_id) DO UPDATE
            SET file_id = $2, updated_at = CURRENT_TIMESTAMP
            """,
            instance_id, file_id
        )

async def get_books_by_author(author: str):
    """Get books by author"""
    return await db.fetch("SELECT * FROM books WHERE author = $1", author)

async def get_books_by_year(year: int):
    """Get books by publication year"""
    return await db.fetch("SELECT * FROM books WHERE year = $1", year)
