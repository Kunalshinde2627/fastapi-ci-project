from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float


items = {}


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    items[item_id] = item
    return {"item_id": item_id, "name": item.name, "price": item.price}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    item = items[item_id]
    return {"item_id": item_id, "name": item.name, "price": item.price}
