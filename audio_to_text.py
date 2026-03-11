# audio_to_text.py
import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load API key from .env

openai.api_key = os.getenv("sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

def audio_to_text(audio_file_path):
    """
    Converts audio (mp3/wav) to transcript text using OpenAI Whisper
    """
    with open(audio_file_path, "rb") as f:
        transcript = openai.Audio.transcriptions.create(
            file=f,
            model="whisper-1"
        )
    return transcript.text
