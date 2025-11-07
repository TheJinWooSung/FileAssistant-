from bot.client import bot
from bot.utils.logger import setup_logger

if __name__ == "__main__":
    logger = setup_logger()
    logger.info("🚀 Starting AI File Assistant Bot...")
    bot.run()
