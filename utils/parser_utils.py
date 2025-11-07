from PyPDF2 import PdfReader
from docx import Document

def extract_text_from_file(file_path: str) -> str:
    """Extract readable text from supported file types."""
    if file_path.endswith(".pdf"):
        reader = PdfReader(file_path)
        return "\n".join([page.extract_text() or "" for page in reader.pages])
    elif file_path.endswith(".docx"):
        doc = Document(file_path)
        return "\n".join([p.text for p in doc.paragraphs])
    else:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
