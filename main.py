from fastapi import FastAPI, Request, HTTPException
from typing import Dict, Any

app = FastAPI()

@app.post("/sendData/")
async def send_data(request: Request):
    """
    Accepts raw JSON input and returns the 'head' part of it.
    """
    try:
        data = await request.json()  # Parse the incoming JSON request body
        return data
    except:
        raise HTTPException(status_code=400, detail="Invalid JSON data")
