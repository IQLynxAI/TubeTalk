import whisper
from utils.logger import logger

# Load Whisper model
whisper_model = whisper.load_model("base")

def transcribe_audio(audio_path):
    """Transcribes audio using Whisper."""
    logger.info(f"Transcribing audio: {audio_path}")
    result = whisper_model.transcribe(audio_path)
    logger.info("Transcription completed")
    return result["text"]