from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import uvicorn
from joblib import load
import numpy as np

app = FastAPI()

# Define a Pydantic model for the incoming data
# class DataModel(BaseModel):
#     data: list[float]

# @app.post("/sendData/")
# async def send_data(data: DataModel):
#     try:
#         with open("posture_model.pkl", "rb") as f:
#             loaded_model = load(f)

#         # Access the 'data' field properly and reshape it
#         input_data = np.array(data.data).reshape(1, -1)

#         # Perform prediction
#         res = loaded_model.predict(input_data)[0]

#         return {"prediction": res}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

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



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
