from fastapi import FastAPI
from openai import OpenAI
from dotenv import load_dotenv
import os
from pydantic import BaseModel
import requests
from requests.models import Response
from typing import List, Optional
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    api_key=OPENAI_API_KEY
)

app = FastAPI()

json_schema = {
    "openapi": "3.1.0",
    "info": {
        "title": "FastAPI",
        "version": "0.1.0"
    },
    "servers": [
        {
            "url": "https://todo-fastapi-beta.vercel.app"
        }
    ],
    "paths": {
        "/create": {
            "post": {
                "summary": "Create Todo",
                "description": "Creates a new todo item.\n\n:param text: The text of the todo item.\n:type text: str\n:param is_complete: Whether the todo item is complete. Defaults to False.\n:type is_complete: bool\n:return: A dictionary containing the text of the new todo item.\n:rtype: dict\n\n:raises ValueError: If the text is empty.",
                "operationId": "create_todo_create_post",
                "parameters": [
                    {
                        "name": "text",
                        "in": "query",
                        "required": True,
                        "schema": {
                            "type": "string",
                            "title": "Text"
                        }
                    },
                    {
                        "name": "is_complete",
                        "in": "query",
                        "required": False,
                        "schema": {
                            "type": "boolean",
                            "default": False,
                            "title": "Is Complete"
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {}
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/todo": {
            "get": {
                "summary": "Get All Todos",
                "description": "Returns a list of all todo items.\n\n:return: A list of todo items.\n:rtype: list\n\n:Example:\n\n>>> get_all_todos()\n[{'id': 1, 'text': 'Buy milk', 'is_done': False}, {'id': 2, 'text': 'Wash dishes', 'is_done': False}]",
                "operationId": "get_all_todos_todo_get",
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {}
                            }
                        }
                    }
                }
            }
        },
        "/done": {
            "get": {
                "summary": "List Done Todos",
                "description": "Returns a list of all done todo items.\n\n:return: A list of done todo items.\n:rtype: list\n\n:Example:\n\n>>> list_done_todos()\n[{'id': 1, 'text': 'Buy milk', 'is_done': True}, {'id': 3, 'text': 'Buy butter', 'is_done': True}]",
                "operationId": "list_done_todos_done_get",
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {}
                            }
                        }
                    }
                }
            }
        },
        "/update/{id}": {
            "patch": {
                "summary": "Update Todo",
                "description": "Updates a todo item.\n\n:param id: Id of the todo item to update.\n:type id: int\n:param text: New text of the todo item(optional).\n:type text: str\n:param is_complete: Completion status of the todo item (optional).\n:type is_complete: bool\n:return: A dictionary containing the id of the updated todo item",
                "operationId": "update_todo_update_id_patch",
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "required": True,
                        "schema": {
                            "type": "integer",
                            "title": "Id"
                        }
                    },
                    {
                        "name": "text",
                        "in": "query",
                        "required": True,
                        "schema": {
                            "type": "string",
                            "title": "Text"
                        }
                    },
                    {
                        "name": "is_complete",
                        "in": "query",
                        "required": False,
                        "schema": {
                            "type": "boolean",
                            "title": "Is Complete"
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {}
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/delete/{id}": {
            "delete": {
                "summary": "Delete Todo",
                "description": "Deletes a todo item.\n\n:param id: The id of the todo item to delete.\n:type id: int\n:return: A dictionary containing the id of the deleted todo item.\n:rtype: dict\n\n:Example:\n\n>>> delete_todo(1)\n{'todo deleted': 1}",
                "operationId": "delete_todo_delete_id_delete",
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "required": True,
                        "schema": {
                            "type": "integer",
                            "title": "Id"
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {}
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                }
            }
        }
    },
    "components": {
        "schemas": {
            "HTTPValidationError": {
                "properties": {
                    "detail": {
                        "items": {
                            "$ref": "#/components/schemas/ValidationError"
                        },
                        "type": "array",
                        "title": "Detail"
                    }
                },
                "type": "object",
                "title": "HTTPValidationError"
            },
            "ValidationError": {
                "properties": {
                    "loc": {
                        "items": {
                            "anyOf": [
                              {
                                  "type": "string"
                              },
                                {
                                  "type": "integer"
                              }
                            ]
                        },
                        "type": "array",
                        "title": "Location"
                    },
                    "msg": {
                        "type": "string",
                        "title": "Message"
                    },
                    "type": {
                        "type": "string",
                        "title": "Error Type"
                    }
                },
                "type": "object",
                "required": [
                    "loc",
                    "msg",
                    "type"
                ],
                "title": "ValidationError"
            }
        }
    }
}

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_api_details",
            "description": "This function gets all the details of an api such as route url, method of the api, query or path parameters, and also body for the post,put, and patch request. ",
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "This is the url of the api with the the endpoint as mentioned in the json schema.",
                    },
                    "method": {
                        "type": "string",
                        "enum": ["get", "post", "patch", "delete"],
                        "description": "This is the method of the api like 'post' 'get' 'patch' 'delete'.",
                    },
                    "body": {
                        "type": "string",
                        "description": "If the value of key 'in' is equal to body, then it is exist. If not, then this is empty string."
                    },
                    "query": {
                        "type": "string",
                        "description": "If the value of key 'in' is equal to query, then it is exist. If not, then this is empty string."
                    }
                },
                "required": ["url", "method", "body", "query"],
            },
        }
    },
]


messages = [
    {"role": "system",
     "content": f'''You are an API extracter which extracts API's from the given schema
     {json_schema} according to the context that what user wanted to do. In this schema, there is list of paths and in each path there is a specific method of http such as "get","post","put","patch","delete". Each method has specific properties which contains a "parameter" object and which is a list of an object containing name of the parameter and also where to pass the parameter. The parameter can be passed to query, body, or in path.  Like for example: User says  dfd
     "Add Breakfast in my todo list" or "I want todo homework" or "Change my todo to something else"
     If the api path's parameter's 'in' value is 'query' then pass the value given by the user to query of the api. And of the api path's parameter's 'in' value is 'body', thenpass the value given by the user to the boddy of the api.
     You need to understand the context of the user and then pull out the write api for that action from
     the given schema. If you are not sure then ask more details from the user! You should not write
     any link from yourself. It should be according to the schema. Ask more questions if you can't
     understand.
     '''},
]


@app.get("/audio")
def transcribe_audio(audio_file_path):
    with open(audio_file_path, 'rb') as audio_file:
        transcription = client.audio.transcriptions.create(
            file=audio_file, model='whisper-1')
    return transcription.text


class Prompt(BaseModel):
    prompt: str


@app.post("/call-api")
def get_response(prompt: Prompt):
    messages.append({"role": "user", "content": prompt.prompt})
    completion = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=messages,
        tools=tools,
    )

    return {"completion": completion, "messages": messages}

# I want to make function that takes url and method as the parameters and returns the completion.


# @app.get("/api-details")
# def get_api_details(url: str, method: str):
#     response = requests.request(method, url)
#     return response

class Message(BaseModel):
    role: str
    content: str


class Messages(BaseModel):
    messages: List[Message]


class ResponseJSON(BaseModel):
    response_json: str


@app.post("/response-audio")
def response_audio(audioResponse: ResponseJSON):
    messages.append({"role": "user", "content": audioResponse.response_json})
    messages.append({
                    "role": "system", "content": "You are responsible to convert the incoming data to spoken language"})
    completion = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=messages,

    )
    return completion
