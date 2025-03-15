from sentence_transformers import SentenceTransformer

# Load embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embeddings(text):
    """Generates embeddings for the given text."""
    return embedding_model.encode(text)