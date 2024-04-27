from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    api_key=OPENAI_API_KEY
)


class OpenAIAssistant:
    client = None
    assistant = None
    thread = None

    def __init__(self, client):
        self.client = client
        self.assistant = client.beta.assistants.create(
            name="API Caller",
            instructions="You are responsible for handling apis for a particular website which will be given by the user. User will give instructions to do particular tasks like 'Add To Cart' 'Tell me the items present in the inventory' 'How many categories are there' ",
            model="gpt-3.5-turbo-0125",
        )
        self.thread = client.beta.threads.create()
