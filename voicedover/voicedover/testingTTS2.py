from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    api_key=OPENAI_API_KEY
)


def TTS(text: str = "Today is a wonderful day to build something people love!"):

    speech_file_path = Path(__file__).parent / "speech.mp3"
    response = client.audio.speech.create(
        model="tts-1",
        voice="onyx",
        input=text
    )

    return response.stream_to_file(speech_file_path)
    # return response.stream_to_file('speech.mp3')


TTS("Just think about all the possibilities of this technology.")
