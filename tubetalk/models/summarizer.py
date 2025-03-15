from transformers import pipeline
import torch
from utils.logger import logger

# Load summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    """Summarizes text using BART."""
    logger.info("Summarizing transcript")
    with torch.no_grad():
        return summarizer(text[:1024])[0]["summary_text"]