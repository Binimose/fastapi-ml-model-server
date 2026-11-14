# FastAPI ML Inference Server
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="ML Model Inference API", version="1.0.0")

class PredictionRequest(BaseModel):
    features: list[float]

@app.post("/predict")
def predict(req: PredictionRequest):
    return {"prediction": sum(req.features) > 0, "confidence": 0.94}
