from fastapi import FastAPI
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
print(OPENAI_API_KEY)

client = OpenAI(
    api_key=OPENAI_API_KEY
)

app = FastAPI()


#the following api will take some text and return the response. It will call openai by passing the api key defined above.
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

