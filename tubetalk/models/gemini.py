import google.generativeai as genai
from utils.logger import logger

# Configure Gemini API
genai.configure(api_key="api_key")

def ask_gemini(context, query):
    """Passes retrieved context and user query to Gemini for final answer."""
    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = f"""
    Given the following context from a video transcript, answer the user's question concisely:

    Context:
    {context}

    Question:
    {query}

    Answer in a clear, to-the-point manner.
    """

    response = model.generate_content(prompt)
    return response.text.strip()