from pyrogram import Client, filters
from bot.utils.parser_utils import extract_text_from_file
from bot.utils.ai_utils import ask_about_file
import os

@Client.on_message(filters.command("ask") & filters.reply)
async def ask_handler(_, message):
    """Ask AI about file content."""
    replied = message.reply_to_message
    if not replied or not replied.document:
        await message.reply_text("📎 Reply to a document with your question, e.g.:\n`/ask What is this about?`")
        return

    query = " ".join(message.command[1:])
    if not query:
        await message.reply_text("❔ You forgot to include a question.")
        return

    file = await replied.download()
    context = extract_text_from_file(file)
    answer = await ask_about_file(query, context)
    await message.reply_text(f"🤖 **Answer:**\n{answer}")
    os.remove(file)
