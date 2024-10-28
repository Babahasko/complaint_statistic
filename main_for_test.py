import asyncio
import uvicorn
from typing import Annotated

from fastapi import FastAPI, Query
from enum import Enum
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


class ModelName(Enum):
    manager = "manager"
    worker = "worker"
    service = "service"


fake_items_db = [
    {"item_name": "Laptop"},
    {"item_name": "Mouse"},
    {"item_name": "Keyboard"},
]


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.model_dump()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


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


@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    results = {
        "items": [{"item_id": "Foo"}, {"item_id": "Bar"}],
    }
    if q:
        results.update({"q": q})
    return results


@app.get("/users/me")
async def read_user_me():
    return {"user_id": f"current_user"}


@app.get("/users/{user_id}")
async def read_user_by_id(user_id: int):
    return {"user_id": user_id}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
