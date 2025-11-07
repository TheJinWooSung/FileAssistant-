from pyrogram.types import ReplyKeyboardMarkup

def main_menu():
    """Return main reply keyboard layout."""
    return ReplyKeyboardMarkup(
        [
            ["📂 Upload File", "🧠 Summarize"],
            ["💬 Ask AI", "ℹ️ Help"]
        ],
        resize_keyboard=True,
        one_time_keyboard=False
    )
