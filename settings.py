from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# Load environment variables first
load_dotenv()

class Settings(BaseSettings):
    """Application settings."""
    BOT_TOKEN: str
    UPSTASH_REDIS_URL: str
    UPSTASH_REDIS_TOKEN: str
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

phrases =[
    "Hmm, I don't quite get that. Try /help or /menu!",
    "I'm not sure what you mean—type /help or /menu for options.",
    "Oops, I didn't understand. Use /help or /menu to see what I can do.",
    "Sorry, that went over my head. Check /help or /menu!",
    "I don't understand that command. Try /help or /menu.",
    "That's unfamiliar to me. Use /help or /menu for guidance.",
    "I'm lost—please use /help or /menu to continue.",
    "I can't parse that. Hit /help or /menu for a list of commands.",
    "Unknown input! Type /help or /menu to get back on track.",
    "I don't recognize that - try /help or /menu.",
    "Sorry, I don't get it. Use /help or /menu to explore.",
    "I'm not following - type /help or /menu to see how I can assist.",
    "Can't process that. Use /help or /menu for help.",
    "That's beyond me. Check /help or /menu!",
    "I don't understand - try /help or /menu to see your options.",
    "I'm confused. Use /help or /menu to find what you need.",
    "Not sure what that is. Type /help or /menu.",
    "I'm stuck - please use /help or /menu.",
    "I don't know that one. Try /help or /menu.",
    "I can't handle that. Use /help or /menu to continue."
]

info_message = (
    "🌟 *About Aaltoes*\n\n"
    "Aaltoes (Aalto Entrepreneurship Society) is the largest student-run entrepreneurship community in Northern Europe. "
    "We are a non-profit organization that helps students and young professionals to develop their entrepreneurial skills "
    "and build their own businesses.\n\n"
    "*Connect with us:*\n"
    "Website: [aaltoes.com](https://aaltoes.com)\n"
    "Instagram: [@aaltoes](https://www.instagram.com/aaltoes/)\n"
    "LinkedIn: [Aaltoes](https://www.linkedin.com/company/aaltoes/)\n"
    "Facebook: [Aaltoes](https://www.facebook.com/aaltoes/)\n"
    "Twitter: [@Aaltoes](https://twitter.com/Aaltoes)\n"
    "Telegram: [@aaltoes](https://t.me/aaltoes)\n\n"
    "📍 *Location:*\n"
    "Aaltoes Startup Sauna\n"
    "Puumiehenkuja 5, 02150 Espoo"
)

help_message = (
    "🤖 *Aaltoes Community Bot Help*\n\n"
    "📱 *Main Commands*\n"
    "/menu \- Open main menu with all actions\n"
    "/help \- Show this help message\n"
    "/info \- Show information about Aaltoes\n\n"  
    "📚 *Library Commands*\n"
    "/books \- Browse available books\n"
    "/borrow \- Borrow a book\n"
    "/return \- Return a book\n"
    "/borrowings \- View your current borrowings\n"
    "/history \- View your borrowing history\n\n"
    "🚪 *Startup Sauna Access*\n"
    "/apply \- Apply for Startup Sauna access\n"
    "/access \- Check your access status\n"
    "/confirm \- Verify your account\n\n"
    "📅 *Events & Reminders*\n"
    "/events \- View upcoming events\n"
    "/reminders \- View your reminders\n\n"
    "👤 *Profile*\n"
    "/profile \- View your profile\n"
    "/change\_name \- Update your name\n\n"   
    "💡 *Tip*: Use /menu for quick access to all features"
)

linear_per_page = 1