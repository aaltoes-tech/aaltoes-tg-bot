from datetime import datetime
from typing import List, Dict, Optional
from db import db
import logging

class PointsRepository:
    def __init__(self):
        self.table_name = "points"
        self.valid_states = ['added', 'removed']
    
    async def init(self, db) -> None:
        """Initialize the points table"""
        try:
            await db.execute(f"""
                CREATE TABLE IF NOT EXISTS {self.table_name} (
                    id SERIAL PRIMARY KEY,
                    user_id BIGINT NOT NULL,
                    state TEXT NOT NULL DEFAULT 'added' CHECK (state IN ('added', 'removed')),
                    points INT NOT NULL DEFAULT 0,
                    time TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES tg_user(id)
                )
            """)
            logging.info(f"Table {self.table_name} initialized successfully")
        except Exception as e:
            logging.error(f"Error initializing table: {e}")
            raise
    
    async def add_points(self, db, user_id: int, points: int) -> None:
        """Add points to a user"""
        await db.execute(f"""
            INSERT INTO {self.table_name} (user_id, points)
            VALUES ($1, $2)
        """, user_id, points)

    async def remove_points(self, db, user_id: int, points: int) -> None:
        """Remove points from a user"""
        await db.execute(f"""
            INSERT INTO {self.table_name} (user_id, points, state)
            VALUES ($1, $2, 'removed')
        """, user_id, points)