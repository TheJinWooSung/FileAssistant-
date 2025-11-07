import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Centralized configuration class for environment variables."""

    API_ID = int(os.getenv("API_ID", "12345"))
    API_HASH = os.getenv("API_HASH", "")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    MONGO_URI = os.getenv("MONGO_URI", "")
    ADMINS = list(map(int, os.getenv("ADMINS", "").split())) if os.getenv("ADMINS") else []

    STORAGE_PATH = "data/files"
    EMBEDDINGS_PATH = "data/embeddings"
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///data/db.sqlite3")

    DEBUG = os.getenv("DEBUG", "false").lower() == "true"
