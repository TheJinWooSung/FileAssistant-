from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("start"))
async def start_handler(_, message: Message):
    await message.reply_text(
        "👋 **Welcome to AI File Assistant Bot!**\n\n"
        "📂 Upload any file and use commands like:\n"
        "• `/summarize` — Summarize your document\n"
        "• `/ask` — Ask questions about it\n"
        "• `/search` — Search through your files\n\n"
        "⚙️ Type `/help` to see all commands."
    )
