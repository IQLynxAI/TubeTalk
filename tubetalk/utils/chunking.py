import nltk
from nltk.tokenize import sent_tokenize

# Download NLTK data
nltk.download("punkt")

def semantic_chunking(text, chunk_size=5):
    """Splits text into semantically meaningful chunks."""
    sentences = sent_tokenize(text)
    chunks = [" ".join(sentences[i:i + chunk_size]) for i in range(0, len(sentences), chunk_size)]
    return chunks