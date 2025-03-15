import faiss
import numpy as np
import pickle
import os
from utils.logger import logger
from models.embedding_model import get_embeddings
from utils.chunking import semantic_chunking
from rank_bm25 import BM25Okapi
from models.gemini import ask_gemini

# Ensure the `data/` directory exists
data_dir = "data"
os.makedirs(data_dir, exist_ok=True)  # Create directory if it doesn't exist

# Initialize FAISS index
d = 384  # Embedding dimension
faiss_index = faiss.IndexFlatL2(d)
video_data = {}

# Load stored embeddings if available
embeddings_path = os.path.join(data_dir, "embeddings.pkl")
if os.path.exists(embeddings_path):
    with open(embeddings_path, "rb") as f:
        video_data = pickle.load(f)
        logger.info("Loaded cached embeddings from disk")

def store_in_faiss(video_id, transcript):
    """Embeds transcript and stores it in FAISS."""
    if video_id in video_data:
        logger.info(f"Embeddings already exist for video ID: {video_id}, skipping processing.")
        return

    logger.info(f"Generating embeddings for new video ID: {video_id}")

    # Apply semantic chunking
    chunks = semantic_chunking(transcript)
    embeddings = get_embeddings(chunks)
    faiss_index.add(np.array(embeddings, dtype=np.float32))

    # Store BM25 index
    tokenized_chunks = [chunk.split() for chunk in chunks]
    bm25 = BM25Okapi(tokenized_chunks)

    video_data[video_id] = {"chunks": chunks, "embeddings": embeddings, "bm25": bm25}

    # Persist embeddings to disk
    with open(embeddings_path, "wb") as f:
        pickle.dump(video_data, f)
        logger.info("Stored embeddings to disk")

def hybrid_search_with_gemini(query):
    """Retrieves relevant transcript chunks using FAISS + BM25 and refines with Gemini."""
    if not video_data:
        return "No data available."

    logger.info(f"Retrieving relevant text for query: {query}")
    query_embedding = get_embeddings([query])
    D, I = faiss_index.search(np.array(query_embedding, dtype=np.float32), k=5)

    # Combine FAISS + BM25 results
    video_id = list(video_data.keys())[0]
    bm25_scores = video_data[video_id]["bm25"].get_scores(query.split())
    sorted_chunks = sorted(zip(video_data[video_id]["chunks"], bm25_scores), key=lambda x: x[1], reverse=True)[:5]
    retrieved_text = "\n".join([chunk for chunk, _ in sorted_chunks] + [video_data[video_id]["chunks"][idx] for idx in I[0]])

    final_response = ask_gemini(retrieved_text, query)

    return final_response