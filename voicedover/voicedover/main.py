from fastapi import FastAPI
from openai import OpenAI
import os
print(os.environ.OPENAI_API_KEY)
# app = FastAPI()
# client = OpenAI(api_key=OPENAI_API_KEY)


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
