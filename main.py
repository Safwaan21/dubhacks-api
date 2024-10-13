from fastapi import FastAPI
from typing import Dict, Any

app = FastAPI()

@app.post("/sendData/")
async def send_data(data: Dict[str, Any]):
    """
    Accepts JSON input and returns the same JSON as a response.
    """
    return {"received_data": data}
