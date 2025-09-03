from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseModel):
    bot_token: str = os.getenv("BOT_TOKEN", "")
    channel_username: str = os.getenv("CHANNEL_USERNAME", "")
    audd_api_token: str | None = os.getenv("AUDD_API_TOKEN")
    database_url: str = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./bot.db")

settings = Settings()
