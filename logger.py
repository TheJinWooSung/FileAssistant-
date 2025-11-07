import logging
import os

def setup_logger():
    """Sets up a clean, professional logging system."""
    os.makedirs("logs", exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] [%(levelname)s] %(name)s: %(message)s",
        handlers=[
            logging.FileHandler("logs/bot.log", mode="a", encoding="utf-8"),
            logging.StreamHandler()
        ]
    )
    logging.getLogger("pyrogram").setLevel(logging.WARNING)
    return logging.getLogger("AIFileBot")
