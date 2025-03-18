import logging
import asyncpg
from typing import Optional

class Database:
    def __init__(self):
        self.pool: Optional[asyncpg.Pool] = None
    
    async def connect(self, database_url: str) -> None:
        """Create a connection pool to the PostgreSQL database"""
        if not database_url:
            logging.warning("DATABASE_URL is not set. Database functionality will be disabled.")
            return
        
        try:
            # Create a connection pool
            self.pool = await asyncpg.create_pool(
                database_url,
                min_size=5,
                max_size=20
            )
            
            # Test the connection
            async with self.pool.acquire() as conn:
                version = await conn.fetchval("SELECT version();")
                logging.info(f"Successfully connected to PostgreSQL: {version}")
        except Exception as e:
            logging.error(f"Failed to create database connection pool: {e}")
            self.pool = None
    
    async def close(self) -> None:
        """Close the database connection pool"""
        if self.pool:
            await self.pool.close()
            logging.info("Database connection pool closed")
    
    async def execute(self, query: str, *args) -> str:
        """Execute a query"""
        if not self.pool:
            logging.error("Database connection not established")
            return None
        
        async with self.pool.acquire() as conn:
            return await conn.execute(query, *args)
    
    async def fetch(self, query: str, *args) -> list:
        """Fetch multiple rows"""
        if not self.pool:
            logging.error("Database connection not established")
            return []
        
        async with self.pool.acquire() as conn:
            return await conn.fetch(query, *args)
    
    async def fetchrow(self, query: str, *args) -> dict:
        """Fetch a single row"""
        if not self.pool:
            logging.error("Database connection not established")
            return None
        
        async with self.pool.acquire() as conn:
            return await conn.fetchrow(query, *args)
    
    async def fetchval(self, query: str, *args):
        """Fetch a single value"""
        if not self.pool:
            logging.error("Database connection not established")
            return None
        
        async with self.pool.acquire() as conn:
            return await conn.fetchval(query, *args)

# Create a single instance to be used throughout the application
db = Database()