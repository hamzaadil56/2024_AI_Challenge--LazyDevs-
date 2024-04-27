from fastapi import FastAPI
from openai import OpenAI
from dotenv import load_dotenv
from voicedover.openai_assistant import OpenAIAssistant
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    api_key=OPENAI_API_KEY
)

app = FastAPI()

assistant = client.beta.assistants.create(
    name="API Caller",
    instructions="You are responsible for handling apis for a particular website which will be given by the user. User will give instructions to do particular tasks like 'Add To Cart' 'Tell me the items present in the inventory' 'How many categories are there' ",
    model="gpt-3.5-turbo-0125",
)

thread = client.beta.threads.create()

message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="I want to order this item of bag!"
)


audio_file_path = './EarningsCall.wav'


@app.get("/{prompt}")
def get_response(prompt):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
            {"role": "user", "content": prompt}
        ]
    )

    return completion.choices[0].message


@app.get("/audio")
def transcribe_audio(audio_file_path):
    with open(audio_file_path, 'rb') as audio_file:
        transcription = client.audio.transcriptions.create(
            "whisper-1", audio_file)
    print(transcription)
    return transcription['text']

# Example usage:
# python main.py
# following function will take in input from the user and send it to openAi client. The response will then be displayed.


@app.get("/chat")
def chat():
    user_input = input("Enter your message: ")
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    )
    print(response.choices[0].message.content)
    return response.choices[0].message.content
