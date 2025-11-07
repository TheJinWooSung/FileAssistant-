from openai import OpenAI
from bot.config import Config

client = OpenAI(api_key=Config.OPENAI_API_KEY)

async def summarize_text(text: str) -> str:
    """Summarize given text content using OpenAI GPT model."""
    if not text.strip():
        return "⚠️ Empty text, nothing to summarize."

    completion = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "Summarize the content concisely and clearly."},
            {"role": "user", "content": text}
        ],
    )
    return completion.choices[0].message.content.strip()

async def ask_about_file(query: str, context: str) -> str:
    """Ask a question about uploaded file content."""
    completion = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant answering based on the provided file context."},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}"}
        ],
    )
    return completion.choices[0].message.content.strip()
