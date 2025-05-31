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
                    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
                    role TEXT DEFAULT 'user',
                    confirm BOOLEAN DEFAULT FALSE,
                    points INT DEFAULT 0
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
            return await self.get_user(user_id)
        except Exception as e:
            logging.error(f"Failed to save user: {e}")
            return False
    
    async def update_user(self, user_id: int, **kwargs):
        """Update a user"""
        try:
            update_fields = []
            values = []
            param_count = 1
            
            for key, value in kwargs.items():
                update_fields.append(f"{key} = ${param_count}")
                values.append(value)
                param_count += 1
            
            values.append(user_id)  # Add user_id as the last parameter
            update_fields = ", ".join(update_fields)
            
            query = f"UPDATE tg_user SET {update_fields} WHERE id = ${param_count}"
            await self.db.execute(query, *values)
            return True
        except Exception as e:
            logging.error(f"Failed to update user: {e}")
            return False
    async def update_points(self, user_id: int, points: int):
        """Update points for a user by adding points in a single query"""
        try:
            await self.db.execute(
                "UPDATE tg_user SET points = COALESCE(points, 0) + $1 WHERE id = $2",
                points, user_id
            )
            return True
        except Exception as e:
            logging.error(f"Failed to update points: {e}")
            return False
    
    async def get_admins(self):
        """Get all admins"""
        try:
            return await self.db.fetch("SELECT id FROM tg_user WHERE role = 'admin'")
        except Exception as e:
            logging.error(f"Failed to get admins: {e}")
            return []
        
    async def is_admin(self, user_id: int) -> bool:
        """Check if a user is an admin"""
        try:
            result = await self.db.fetchrow("SELECT role FROM tg_user WHERE id = $1", user_id)
            return result and result['role'] == 'admin'
        except Exception as e:
            logging.error(f"Failed to check if user is admin: {e}")
            return False
        
    async def set_admin(self, user_id: int):
        """Set a user as admin"""
        try:
            await self.db.execute("UPDATE tg_user SET role = 'admin' WHERE id = $1", user_id)
        except Exception as e:
            logging.error(f"Failed to set admin: {e}")
    
    async def get_user(self, user_id: int):
        """Get a user by ID"""
        try:
            return await self.db.fetchrow("SELECT * FROM tg_user WHERE id = $1", user_id)
        except Exception as e:
            logging.error(f"Failed to get user: {e}")
            return None
