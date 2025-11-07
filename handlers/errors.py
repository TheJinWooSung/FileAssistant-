import asyncio
import logging
from pyrogram import Client
from pyrogram.errors import FloodWait, RPCError

logger = logging.getLogger(__name__)

@Client.on_message()
async def global_error_handler(client, message):
    """
    Global message error handler.
    Ensures bot won’t crash on FloodWait or random Pyrogram errors.
    """
    try:
        await message.continue_propagation()
    except FloodWait as e:
        logger.warning(f"FloodWait: sleeping for {e.value} seconds.")
        await asyncio.sleep(e.value)
    except RPCError as e:
        logger.error(f"Telegram API Error: {e}")
        try:
            await message.reply_text("⚠️ Telegram is rate-limiting me. Try again soon.")
        except Exception:
            pass
    except Exception as e:
        logger.exception(f"Unhandled error: {e}")
        try:
            await message.reply_text("❌ Unexpected internal error. Please try again later.")
        except Exception:
            pass
