from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Any, Dict
import logging 

app = FastAPI()

# Define the expected structure of the incoming JSON
class RequestBody(BaseModel):
    data: Dict[str, Any]  # The body will contain a "data" field holding the object

@app.post("/sendData/")
async def send_data(body: RequestBody):
    """
    Accepts JSON input with a "data" field and returns the "head" data from it.
    """
    logging.debug(f"Received data: {body}")

    return {"check": body}
