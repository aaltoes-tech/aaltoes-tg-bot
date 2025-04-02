from datetime import datetime
from typing import List, Dict, Any
import pytz

class RemindersRepository:
    def __init__(self):
        self.table_name = "reminders"
    
    async def init(self, db) -> None:
        """Initialize the reminders table"""
        await db.execute(f"""
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                id SERIAL PRIMARY KEY,
                user_id BIGINT NOT NULL,
                event_id TEXT NOT NULL,
                reminder_time TIMESTAMP WITH TIME ZONE NOT NULL,
                created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(user_id, event_id)
            )
        """)
    
    async def save_reminder(self, db, user_id: int, event_id: str, reminder_time: datetime) -> None:
        """Save a new reminder to the database"""
        await db.execute(
            f"""
            INSERT INTO {self.table_name} (user_id, event_id, reminder_time)
            VALUES ($1, $2, $3)
            ON CONFLICT (user_id, event_id) DO UPDATE
            SET reminder_time = $3
            """,
            user_id, event_id, reminder_time
        )
    
    async def get_reminders(self, db) -> List[Dict[str, Any]]:
        """Get all active reminders"""
        return await db.fetch(f"""
            SELECT * FROM {self.table_name}
            WHERE reminder_time > CURRENT_TIMESTAMP
            ORDER BY reminder_time ASC
        """)
    
    async def delete_reminder(self, db, user_id: int, event_id: str) -> None:
        """Delete a reminder from the database"""
        await db.execute(
            f"DELETE FROM {self.table_name} WHERE user_id = $1 AND event_id = $2",
            user_id, event_id
        )
    
    async def get_user_reminders(self, db, user_id: int) -> List[Dict[str, Any]]:
        """Get all reminders for a specific user"""
        return await db.fetch(
            f"SELECT * FROM {self.table_name} WHERE user_id = $1",
            user_id
        ) 