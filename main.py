from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import uvicorn
from joblib import load
import numpy as np
import logging

app = FastAPI()

logger = logging.getLogger(__name__)

@app.post("/sendData/")
async def send_data(request: Request):
    """
    Accepts raw JSON input and returns the 'head' part of it.
    """
    try:
        data = await request.json()  # Parse the incoming JSON request body
        logger.info(f"Received data: {data}")
        # Print the type and check if it's a string or a dictionary

        if type(data) == str:
            return {"head": "String"}
        else:
            return {"head": data["head"].keys()}

        return {"head": data["head"]}
        input_data = np.array(data["data"]).reshape(1, -1)

        with open("posture_model.pkl", "rb") as f:
            loaded_model = load(f)
            res = loaded_model.predict(input_data)[0]

        return {"prediction": res}
    except:
        raise HTTPException(status_code=400, detail="Invalid JSON data")



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
