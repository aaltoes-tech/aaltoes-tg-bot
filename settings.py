from dotenv import load_dotenv
from pydantic_settings import BaseSettings
import os

# Load environment variables first
load_dotenv()

class Settings(BaseSettings):
    """Application settings."""
    BOT_TOKEN: str = "8055720065:AAFsW1SP3TuQVcFgMoNFo1rNQI5qtaZ8vuk"
    DATABASE_URL: str | None = None
    DATABASE_URL_UNPOOLED: str
    LUMA_API_KEY: str
    ADMINS: list[str] = [
        '658415666', '468596234'
    ]

    class Config:
        env_file = ".env"
        extra = "ignore"  # This will ignore extra environment variables

# Initialize settings
settings = Settings()
