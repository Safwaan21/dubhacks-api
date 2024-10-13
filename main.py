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
        head_data = data.get("head")  # Extract the 'head' field from the JSON
        if head_data is None:
            raise HTTPException(status_code=400, detail="'head' not found in the data")
        return head_data  # Return the 'head' part as response
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid JSON: {str(e)}")

