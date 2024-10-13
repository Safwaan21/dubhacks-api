from fastapi import FastAPI
from typing import Dict, Any
import json
app = FastAPI()

@app.post("/sendData/")
async def send_data(data: str):
    """
    Accepts JSON input and returns the same JSON as a response.
    """
    body = json.loads(data)
    return {"received_data": data}
