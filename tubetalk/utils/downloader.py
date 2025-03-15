import yt_dlp
from utils.logger import logger

def download_audio(url):
    """Downloads audio from a YouTube video."""
    logger.info(f"Downloading audio from {url}")
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "audio.%(ext)s",
        "postprocessors": [{"key": "FFmpegExtractAudio", "preferredcodec": "wav"}],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        logger.info(f"Downloaded video ID: {info['id']}")
        return "audio.wav", info["id"]