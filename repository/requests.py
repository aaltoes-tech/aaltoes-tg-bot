from datetime import datetime
from typing import List, Dict, Optional
from db import db
import logging

class RequestsRepository:
    def __init__(self):
        self.table_name = "access_requests"
        self.valid_states = ['applied', 'pending', 'approved', 'rejected']
    
    async def init(self, db) -> None:
        """Initialize the access_requests table"""
        try:
            await db.execute(f"""
                CREATE TABLE IF NOT EXISTS {self.table_name} (
                    request_id SERIAL PRIMARY KEY,
                    user_id BIGINT NOT NULL,
                    motivation TEXT NOT NULL,
                    secret_word TEXT,
                    state TEXT NOT NULL DEFAULT 'applied',
                    request_time TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES tg_user(id)
                )
            """)
            logging.info(f"Table {self.table_name} initialized successfully")
        except Exception as e:
            logging.error(f"Error initializing {self.table_name} table: {e}")
            raise

    async def create_request(self, db, user_id: int, motivation: str, secret_word: Optional[str] = None) -> int:
        """Create a new access request"""
        try:
            result = await db.fetch(
                f"""
                INSERT INTO {self.table_name} (user_id, motivation, secret_word, state)
                VALUES ($1, $2, $3, 'applied')
                RETURNING request_id
                """,
                user_id, motivation, secret_word
            )
            return result[0]['request_id']
        except Exception as e:
            logging.error(f"Error creating request: {e}")
            raise

    async def get_user_access(self, db, user_id: int) -> Optional[Dict]:
        """Get all access requests for a user"""
        try:
            result = await db.fetch(
                f"""
                SELECT * FROM {self.table_name}
                WHERE user_id = $1 AND state = 'approved' 
                ORDER BY request_time DESC
                """,
                user_id
            )
            # Check if result is empty
            if not result or len(result) == 0:
                return None
            return result[0]
        
        except Exception as e:
            logging.error(f"Error getting user access: {e}")
            raise
        
    async def get_user_last_request(self, db, user_id: int) -> Optional[Dict]:
        """Get the last request for a user"""
        try:
            result = await db.fetch(
                f"""
                SELECT * FROM {self.table_name}
                WHERE user_id = $1 ORDER BY request_time DESC LIMIT 1
                """,
                user_id
            )
            return result[0] if result else None
        except Exception as e:
            logging.error(f"Error getting user last request: {e}")
            raise   
    
    async def get_users_with_access(self, db) -> List[Dict]:
        """Get all users with access"""
        try:
            return await db.fetch(
                f"""
                SELECT u.username, r.secret_word, r.user_id
                FROM {self.table_name} r
                JOIN tg_user u ON r.user_id = u.id
                WHERE r.state = 'approved'
                """)
        except Exception as e:
            logging.error(f"Error getting users with access: {e}")
            raise

    async def get_user_active_requests(self, db, user_id: int) -> List[Dict]:
        """Get all requests for a user"""
        try:
            return await db.fetch(
                f"""
                SELECT * FROM {self.table_name}
                WHERE user_id = $1 AND (state = 'pending' OR state = 'applied')
                ORDER BY request_time DESC
                """,
                user_id
            )
        except Exception as e:
            logging.error(f"Error getting user requests: {e}")
            raise

    async def get_pending_requests(self, db) -> List[Dict]:
        """Get all pending requests"""
        try:
            return await db.fetch(
                f"""
                SELECT * FROM {self.table_name}
                WHERE state = 'pending'
                ORDER BY request_time ASC
                """
            )
        except Exception as e:
            logging.error(f"Error getting pending requests: {e}")
            raise

    async def get_request_by_id(self, db, request_id: int) -> Optional[Dict]:
        """Get a request by its ID"""
        try:
            result = await db.fetch(
                f"""
                SELECT * FROM {self.table_name}
                WHERE request_id = $1
                """,
                request_id
            )
            return result[0] if result else None
        except Exception as e:
            logging.error(f"Error getting request by ID: {e}")
            raise

    async def update_request_state(self, db, request_id: int, state: str) -> None:
        """Update request state"""
        try:
            await db.execute(
                f"UPDATE {self.table_name} SET state = $1::text WHERE request_id = $2::integer",
                str(state),  # Explicitly cast to string
                int(request_id)  # Explicitly cast to integer
            )
        except Exception as e:
            logging.error(f"Error updating request state: {e}")
            raise
        
    async def suspend_access(self, db, user_id: int) -> None:
        """Suspend access for a user"""
        try:
            await db.execute(
                f"""
                UPDATE {self.table_name}
                SET state = 'rejected'
                WHERE user_id = $1
                """,
                user_id
            )
        except Exception as e:
            logging.error(f"Error suspending access: {e}")
            raise

    async def get_applied_requests(self, db) -> List[Dict]:
        """Get all applied requests"""
        try:
            return await db.fetch(f"""
                SELECT r.*, u.username, u.name
                FROM {self.table_name} r
                JOIN tg_user u ON r.user_id = u.id
                WHERE r.state = 'applied'
                ORDER BY r.request_time ASC
            """)
        except Exception as e:
            logging.error(f"Error getting applied requests: {e}")
            raise

    async def get_approved_requests(self, db) -> List[Dict]:
        """Get all approved requests"""
        try:
            return await db.fetch(f"""
                SELECT r.*, u.username, u.name
                FROM {self.table_name} r
                JOIN tg_user u ON r.user_id = u.id
                WHERE r.state = 'approved'
                ORDER BY r.request_time ASC
            """)
        except Exception as e:
            logging.error(f"Error getting approved requests: {e}")
            raise

    async def get_rejected_requests(self, db) -> List[Dict]:
        """Get all rejected requests"""
        try:
            return await db.fetch(f"""
                SELECT r.*, u.username, u.name
                FROM {self.table_name} r
                JOIN tg_user u ON r.user_id = u.id
                WHERE r.state = 'rejected'
                ORDER BY r.request_time ASC
            """)
        except Exception as e:
            logging.error(f"Error getting rejected requests: {e}")
            raise
    