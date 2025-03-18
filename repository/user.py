import logging
from db import Database

class UserRepository:
    async def init(self, db: Database):
        self.db = db
        """Initialize the user table if it doesn't exist"""
        try:
            await self.db.execute("""
                CREATE TABLE IF NOT EXISTS tg_user (
                    id BIGINT PRIMARY KEY,
                    username TEXT,
                    name TEXT,
                    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
                )
            """)
            logging.info("User table initialized")
        except Exception as e:
            logging.error(f"Failed to initialize user table: {e}")
    
    async def save_user(self, user_id: int, username: str | None, name: str):
        """Create or update a user"""
        if username is None:
            username = ""
        try:
            logging.info(f"Saving user: {user_id}, {username}, {name}")
            await self.db.execute("""
                INSERT INTO tg_user (id, username, name) 
                VALUES ($1, $2, $3)
                ON CONFLICT (id) 
                DO UPDATE SET username = $2, name = $3
            """, user_id, username, name)
            return True
        except Exception as e:
            logging.error(f"Failed to save user: {e}")
            return False
    
    async def get_user(self, user_id: int):
        """Get a user by ID"""
        try:
            return await self.db.fetchrow("SELECT * FROM tg_user WHERE id = $1", user_id)
        except Exception as e:
            logging.error(f"Failed to get user: {e}")
            return None
