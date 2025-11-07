import os
from datetime import datetime

def save_file(document, user_id: int, download_fn):
    """Save user-uploaded files in organized structure."""
    user_folder = f"data/files/{user_id}"
    os.makedirs(user_folder, exist_ok=True)

    file_path = f"{user_folder}/{datetime.now().strftime('%Y%m%d_%H%M%S')}_{document.file_name}"
    return download_fn(file_path)
