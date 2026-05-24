from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np
import os

# Auto-train model if not found
if not os.path.exists("diamond_model.pkl"):
    import train
app = FastAPI(title="Diamond Price Predictor API")

# Allow frontend to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the trained model
model = joblib.load("diamond_model.pkl")

# Input schema
class DiamondInput(BaseModel):
    carat: float
    cut: int       # 1=Fair, 2=Good, 3=Very Good, 4=Premium, 5=Ideal
    color: int     # 1=J ... 7=D
    clarity: int   # 1=I2 ... 10=FL
    depth: float = 61.7
    table: float = 57.0
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0

@app.get("/health")
def health():
    return {"status": "online", "model": "Random Forest Diamond Predictor"}

@app.post("/predict")
def predict(diamond: DiamondInput):
    features = np.array([[
        diamond.carat, diamond.cut, diamond.color, diamond.clarity,
        diamond.depth, diamond.table, diamond.x, diamond.y, diamond.z
    ]])
    log_price = model.predict(features)[0]
    price = float(np.exp(log_price))
    low   = round(price * 0.87)
    high  = round(price * 1.13)
    return {
        "predicted_price": round(price),
        "range_low":  low,
        "range_high": high,
        "currency": "USD"
    }