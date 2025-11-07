from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def help_inline():
    """Return inline help menu buttons."""
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🧠 Summarize", callback_data="summarize_help")],
        [InlineKeyboardButton("💬 Ask AI", callback_data="ask_help")],
        [InlineKeyboardButton("📂 Upload Files", callback_data="upload_help")],
        [InlineKeyboardButton("💻 Source Code", url="https://github.com/TheJinWooSung/FileAssistant")]
    ])
