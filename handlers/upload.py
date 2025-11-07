from pyrogram import Client, filters
from pyrogram.types import Message
from bot.utils.file_utils import save_file
from bot.utils.logger import setup_logger

logger = setup_logger()

@Client.on_message(filters.document)
async def handle_file_upload(client: Client, message: Message):
    """Handles user file uploads and saves them."""
    await message.reply_chat_action("upload_document")
    try:
        file_path = await save_file(message.document, message.from_user.id, message.download)
        await message.reply_text(f"✅ File saved successfully!\n📄 Path: `{file_path}`")
        logger.info(f"User {message.from_user.id} uploaded {message.document.file_name}")
    except Exception as e:
        logger.error(f"Error saving file: {e}")
        await message.reply_text("❌ Failed to process your file. Please try again.")
