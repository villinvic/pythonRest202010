from typing import Optional
from fastapi import FastAPI

from model import Item

app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items")
def read_all_items():
    return [ {'item_id': 3, "name": "tablette"},
            {'item_id': 4, "name": "cable HDMI"} ]

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {'item_id': item_id, "q": q}

@app.post("/items")
def post_item(item: Item):
    #return {'item_name': item.name, "status": "new"}
    return item

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    #return {'item_id': item_id, "modified": q}
    return item

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    # possible to return object to delete
    return True







