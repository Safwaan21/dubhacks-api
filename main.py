from fastapi import FastAPI
from typing import Dict, Any
import json
app = FastAPI()

# class Item(BaseModel):
#     name: str
#     price: float

# @app.post("/items/")
# def create_item(item: Item):
#     return item  # FastAPI automatically converts this to JSON

@app.post("/sendData/")
async def send_data(data: str):
    print(f"[safwaans-test]: {data}")
    """
    Accepts JSON input and returns the same JSON as a response.
    """
    return {"received_data": data["head"]}
