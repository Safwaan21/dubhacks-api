# main.py
from fastapi import FastAPI, Depends, HTTPException, Request
import pickle
app = FastAPI()


@app.post("/sendData/")
async def send_data(request: Request):
    loaded_model = pickle.load(open("posture_model.pkl", "rb"))
    """
    Accepts raw JSON input and returns the 'head' part of it.
    """
    try:
        data = await request.json()  # Parse the incoming JSON request body
        res = loaded_model.predict(data["data"])
        return res
    except:
        raise HTTPException(status_code=400, detail="Invalid JSON data")
