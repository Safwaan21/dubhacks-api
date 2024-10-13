from fastapi import FastAPI, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from .database import Base, engine, get_db
from .models import RequestEntry
from typing import Dict, Any

app = FastAPI()
Base.metadata.create_all(bind=engine)


@app.post("/sendData/")
async def send_data(request: Request):
    """
    Accepts raw JSON input and returns the 'head' part of it.
    """
    try:
        data = await request.json()  # Parse the incoming JSON request body
        return data["data"]
    except:
        raise HTTPException(status_code=400, detail="Invalid JSON data")
