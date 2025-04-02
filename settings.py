from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    """Application settings."""
    BOT_TOKEN: str
    DATABASE_URL: str | None = None
    LUMA_API_KEY: str

# Initialize settings
settings = Settings()