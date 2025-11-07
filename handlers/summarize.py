from pyrogram import Client, filters
from bot.utils.parser_utils import extract_text_from_file
from bot.utils.ai_utils import summarize_text
import os

@Client.on_message(filters.command("summarize") & filters.reply)
async def summarize_document(_, message):
    """Summarize the replied-to document."""
    replied = message.reply_to_message
    if not replied or not replied.document:
        await message.reply_text("📎 Reply to a document to summarize it.")
        return

    file = await replied.download()
    text = extract_text_from_file(file)
    summary = await summarize_text(text)
    await message.reply_text(f"🧠 Summary:\n\n{summary[:4000]}")
    os.remove(file)
