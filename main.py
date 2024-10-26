import asyncio
import uvicorn
from fastapi import FastAPI
from enum import Enum

app = FastAPI()


class ModelName(Enum):
    manager = "manager"
    worker = "worker"
    service = "service"


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/model/{model_name}")
async def get_model(model_name: ModelName):
    match model_name:
        case model_name.manager:
            return {
                "model_name": model_name,
                "message": "Hi dear manager",
            }
        case model_name.worker:
            return {
                "model_name": model_name,
                "message": "Hi dear workers",
            }
        case model_name.service:
            return {
                "model_name": model_name,
                "message": "Hi dear service",
            }
        case _:
            return {"message": "I don`t know who you are"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/users/me")
async def read_user_me():
    return {"user_id": f"current_user"}


@app.get("/users/{user_id}")
async def read_user_by_id(user_id: int):
    return {"user_id": user_id}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
