from datetime import datetime, timedelta
from typing import List, Dict, Optional, Any
from db import db
import logging

class BorrowingsRepository:
    def __init__(self):
        self.table_name = "borrowings"
        self.instances_table_name = "books_instances"  
        
    async def init(self, db) -> None:
        """Initialize borrowings table"""
        try:
            await db.execute(f"""
                CREATE TABLE IF NOT EXISTS {self.table_name} (
                    borrow_id SERIAL PRIMARY KEY,
                    user_id INTEGER REFERENCES tg_user(id),
                    instance_id INTEGER REFERENCES {self.instances_table_name}(instance_id),
                    borrow_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    borrow_return_time TIMESTAMP,
                    state TEXT DEFAULT 'borrowed',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            logging.info(f"Table {self.table_name} initialized successfully")
        except Exception as e:
            logging.error(f"Error initializing table: {e}")
            raise
        
    async def create_borrowing(self, db, user_id: int, instance_id: int) -> int:
        """Create a new borrowing record"""
        borrow_return_time = datetime.now() + timedelta(days=14)
        return await db.fetchval(f"""
            INSERT INTO {self.table_name} (user_id, instance_id, borrow_return_time, state)
            VALUES ($1, $2, $3, 'borrowed')
            RETURNING borrow_id
        """, user_id, instance_id, borrow_return_time)
        
    async def get_user_borrowings(self, db, user_id: int) -> List[Dict]:
        """Get all borrowings for a user"""
        return await db.fetch(f"""
            SELECT b.*, bi.book_id, bk.title, bk.author, bi.instance_id
            FROM {self.table_name} b
            JOIN {self.instances_table_name} bi ON b.instance_id = bi.instance_id
            JOIN books bk ON bi.book_id = bk.book_id
            WHERE b.user_id = $1 AND b.state IN ('borrowed', 'overdue')
            ORDER BY b.borrow_time DESC
        """, user_id)
    async def get_user_borrowings_history(self, db, user_id: int) -> List[Dict]:
        """Get all borrowings for a user"""
        return await db.fetch(f"""
            SELECT b.*, bi.book_id, bk.title, bk.author, bi.instance_id
            FROM {self.table_name} b
            JOIN {self.instances_table_name} bi ON b.instance_id = bi.instance_id
            JOIN books bk ON bi.book_id = bk.book_id
            WHERE b.user_id = $1
            ORDER BY b.borrow_time DESC
        """, user_id)

    async def get_user_pending_borrowings(self, db, user_id: int) -> List[Dict[str, Any]]:
        """Get all pending borrowings for a specific user"""
        return await db.fetch(f"""
            SELECT b.*, bk.title, bk.author, bi.instance_id
            FROM {self.table_name} b
            JOIN {self.instances_table_name} bi ON b.instance_id = bi.instance_id
            JOIN books bk ON bi.book_id = bk.book_id
            WHERE b.user_id = $1 AND b.state = 'pending'
            ORDER BY b.borrow_time DESC
        """, user_id)
    
        
    async def get_borrowing_by_instance(self, db, instance_id: int) -> Dict:
        """Get borrowing by instance ID"""
        return await db.fetchrow(f"""
            SELECT b.*, bi.book_id, bk.title, bk.author
            FROM {self.table_name} b
            JOIN {self.instances_table_name} bi ON b.instance_id = bi.instance_id
            JOIN books bk ON bi.book_id = bk.book_id
            WHERE b.instance_id = $1 AND b.state IN ('borrowed', 'overdue')
        """, instance_id)

    async def get_borrowing_by_id(self, db, borrow_id: int) -> Dict:
        """Get borrowing by ID"""
        return await db.fetchrow(f"""
            SELECT b.*, bi.book_id, bk.title, bk.author, u.username
            FROM {self.table_name} b
            JOIN {self.instances_table_name} bi ON b.instance_id = bi.instance_id
            JOIN books bk ON bi.book_id = bk.book_id 
            JOIN tg_user u ON b.user_id = u.id
            WHERE b.borrow_id = $1
        """, borrow_id)
        
    async def update_borrowing_state(self, db, borrow_id: int, state: str) -> None:
        """Update the state of a borrowing"""
        if state not in ['borrowed', 'pending', 'returned', 'overdue']:
            raise ValueError(f"Invalid state: {state}")
            
        await db.execute(f"""
            UPDATE {self.table_name}
            SET state = $1
            WHERE borrow_id = $2
        """, state, borrow_id)
    async def get_pending_borrowings(self, db) -> List[Dict]:
        """Get all pending borrowings"""
        return await db.fetch(f"""
            SELECT b.*, bi.book_id, bk.title, bk.author
            FROM {self.table_name} b
            JOIN {self.instances_table_name} bi ON b.instance_id = bi.instance_id
            JOIN books bk ON bi.book_id = bk.book_id
            WHERE state = 'pending'
        """)
        
    async def get_overdue_borrowings(self, db) -> List[Dict]:
        """Get all overdue borrowings"""
        try:
            return await db.fetch(f"""
                SELECT b.*, bi.instance_id, bk.title, bk.author, u.username
                FROM {self.table_name} b
                JOIN {self.instances_table_name} bi ON b.instance_id = bi.instance_id
                JOIN books bk ON bi.book_id = bk.book_id
                JOIN tg_user u ON b.user_id = u.user_id
                WHERE b.state = 'overdue'
            """)
        except Exception as e:
            logging.error(f"Error getting overdue borrowings: {e}")
            return []
        
    async def update_overdue_borrowings(self, db) -> None:
        """Update the state of overdue borrowings"""
        await db.execute(f"""
            UPDATE {self.table_name}
            SET state = 'overdue'
            WHERE state IN ('borrowed', 'pending')
            AND borrow_return_time < CURRENT_TIMESTAMP
        """) 