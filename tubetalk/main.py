import streamlit as st
from models.whisper_model import transcribe_audio
from models.summarizer import summarize_text
from utils.downloader import download_audio
from utils.faiss_utils import store_in_faiss, hybrid_search_with_gemini
from utils.logger import logger

"""
Main Streamlit application for YouTube Video Q&A with AI.
This app allows users to input a YouTube video URL, process the video's audio, transcribe it,
and interact with the transcript using AI-powered question answering.
"""

st.title("🎥 YouTube Video Q&A with AI")

video_url = st.text_input("🔗 Enter YouTube Video URL")

if st.button("Process Video"):
    if video_url:
        with st.spinner("Downloading and processing video..."):
            try:
                """
                Downloads the audio from the provided YouTube URL, transcribes it, and stores the transcript
                in a FAISS vector database for semantic search. Displays a summary of the transcript.
                """
                audio_path, video_id = download_audio(video_url)
                st.session_state['video_id'] = video_id
                transcript = transcribe_audio(audio_path)
                store_in_faiss(video_id, transcript)
                st.success("✅ Video processed successfully!")
                logger.info(f"Video processing completed for ID: {video_id}")

                st.write("### 📌 Summary:")
                st.info(summarize_text(transcript))

            except Exception as e:
                logger.error(f"Error processing video: {str(e)}")
                st.error("Failed to process video. Check logs for details.")

if "video_id" in st.session_state:
    """
    Displays the chat interface for interacting with the processed video.
    Users can ask questions about the video, and the app retrieves answers using
    a hybrid search approach (FAISS + BM25) and refines the response using Gemini.
    """
    st.write("## 🗣️ Chat with the Video")
    user_input = st.text_input("Ask a question about the video")

    if st.button("Ask"):
        if user_input:
            try:
                response_text = hybrid_search_with_gemini(user_input)

                st.write("### 🤖 Answer:")
                st.success(response_text)
                logger.info(f"User query: {user_input} | Response: {response_text}")
            except Exception as e:
                logger.error(f"Error in chat response: {str(e)}")
                st.error("Error retrieving response. Check logs.")