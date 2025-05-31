from datetime import datetime
from typing import List, Dict, Optional
from db import db
import logging

class PointsRequestsRepository:
    def __init__(self):
        self.table_name = "points_requests"
        self.valid_states = ['pending', 'approved', 'rejected']
    
    async def init(self, db) -> None:
        """Initialize the access_requests table"""
        try:
            await db.execute(f"""
                CREATE TABLE IF NOT EXISTS {self.table_name} (
                    request_id SERIAL PRIMARY KEY,
                    state TEXT NOT NULL DEFAULT 'pending' CHECK (state IN ('pending', 'approved', 'rejected')),
                    user_id BIGINT NOT NULL,
                    issue_id TEXT NOT NULL,
                    motivation TEXT NOT NULL,
                    points INT NOT NULL DEFAULT 0,
                    request_time TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES tg_user(id)
                )
            """)
            logging.info(f"Table {self.table_name} initialized successfully")
        except Exception as e:
            logging.error(f"Error initializing {self.table_name} table: {e}")
            raise

    async def create_request(self, db, user_id: int, issue_id: str, motivation: str, points: int) -> int:
        """Create a new access request"""
        try:
            result = await db.fetch(
                f"""
                INSERT INTO {self.table_name} (user_id, issue_id, motivation, points)
                VALUES ($1, $2, $3, $4)
                RETURNING request_id
                """,
                user_id, issue_id, motivation, points
            )
            return result[0]['request_id']
        except Exception as e:
            logging.error(f"Error creating request: {e}")
            raise

    async def get_requests(self, db) -> List[Dict]:
        """Get all pending requests"""
        try:
            return await db.fetch(
                f"""
                SELECT pr.request_id, u.username as username, u.name as name, pr.issue_id, pr.motivation, pr.points, pr.request_time
                FROM {self.table_name} pr
                JOIN tg_user u ON pr.user_id = u.id
                WHERE pr.state = 'pending'
                ORDER BY pr.request_time ASC
                """
            )
        except Exception as e:
            logging.error(f"Error getting requests: {e}")
            raise

    async def get_request_by_id(self, db, request_id: int) -> Optional[Dict]:
        """Get a request by its ID"""
        try:
            result = await db.fetch(
                f"""
                SELECT pr.request_id, pr.user_id, u.username as username, u.name as name, pr.issue_id, pr.motivation, pr.points, pr.request_time
                FROM {self.table_name} pr
                JOIN tg_user u ON pr.user_id = u.id
                WHERE pr.request_id = $1
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
    async def get_user_request(self, db, user_id: int, issue_id: str) -> List[Dict]:
        """Get all requests for a user"""
        try:
            result = await db.fetch(
                f"SELECT * FROM {self.table_name} WHERE user_id = $1 AND (state = 'pending' or state = 'approved') AND issue_id = $2",
                user_id, issue_id
            )
            return result[0] if result else None
        except Exception as e:
            logging.error(f"Error getting user requests: {e}")
            raise
    