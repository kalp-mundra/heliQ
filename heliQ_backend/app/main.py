from datetime import datetime
from pathlib import Path
import json
import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "ac_power_xgb.joblib"
METADATA_PATH = BASE_DIR / "models" / "metadata.json"

model = joblib.load(MODEL_PATH)
with open(METADATA_PATH, "r") as f:
    metadata = json.load(f)

FEATURES = metadata["features"]

app = FastAPI(
    title="Heliq Solar Energy Prediction API",
    description="FastAPI backend for photovoltaic AC power prediction.",
    version="1.0.0",
)

class PredictionRequest(BaseModel):
    date_time: datetime
    ambient_temperature: float = Field(..., description="Ambient temperature in °C")
    module_temperature: float = Field(..., description="PV module temperature in °C")
    irradiation: float = Field(..., ge=0, description="Solar irradiation in W/m²")

class PredictionResponse(BaseModel):
    predicted_ac_power: float
    unit: str = "kW"
    timestamp: datetime

def build_features(request: PredictionRequest) -> pd.DataFrame:
    dt = request.date_time
    row = {
        "AMBIENT_TEMPERATURE": request.ambient_temperature,
        "MODULE_TEMPERATURE": request.module_temperature,
        "IRRADIATION": request.irradiation,
        "hour": dt.hour + dt.minute / 60.0,
        "day_of_year": dt.timetuple().tm_yday,
        "month": dt.month,
        "day_of_week": dt.weekday(),
        "is_daylight": int(request.irradiation > 0),
    }
    return pd.DataFrame([row], columns=FEATURES)

@app.get("/health")
def health():
    return {
        "status": "ok",
        "model": "XGBoost",
        "target": metadata["target"],
    }

@app.get("/model-info")
def model_info():
    return metadata

@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    try:
        X = build_features(request)
        prediction = float(model.predict(X)[0])
        prediction = max(0.0, prediction)

        return PredictionResponse(
            predicted_ac_power=round(prediction, 3),
            timestamp=request.date_time,
        )
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
