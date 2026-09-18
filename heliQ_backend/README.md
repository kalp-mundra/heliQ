# Heliq — FastAPI Energy Output Prediction Backend

This backend provides an API for predicting **plant-level AC power output** from weather and time features.

## Dataset used

- Generation data: 68,778 inverter records
- Weather data: 3,182 plant-level weather records
- Generation data contains 22 inverter/source keys.
- The backend training pipeline aggregates the 22 inverter AC power readings at each timestamp to obtain total plant AC power.
- Weather and generation timestamps are merged at 15-minute intervals.

## Why AC_POWER is the prediction target

`AC_POWER` represents instantaneous AC-side generated power and is a better prediction target for a 15-minute forecasting API than `TOTAL_YIELD`, which is cumulative. `DAILY_YIELD` can be added later for daily-energy forecasting.

## Project structure

```text
heliq_backend/
├── app/
│   ├── __init__.py
│   └── main.py
├── data/
│   ├── Plant_1_Generation_Data.csv
│   └── Plant_1_Weather_Sensor_Data.csv
├── models/
│   ├── ac_power_xgb.joblib
│   └── metadata.json
├── requirements.txt
├── train.py
├── run.py
└── README.md
```

## 1. Setup FastAPI backend environment

### Windows

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

If you retrain the model:

```bash
python train.py
```

Start the API:

```bash
python run.py
```

Or:

```bash
uvicorn app.main:app --reload
```

API:

- `GET /health`
- `GET /model-info`
- `POST /predict`
- Swagger UI: `http://127.0.0.1:8000/docs`

## 2. Develop core backend service

### Prediction request

```json
{
  "date_time": "2020-06-15T12:00:00",
  "ambient_temperature": 30.5,
  "module_temperature": 45.2,
  "irradiation": 0.82
}
```

### Prediction response

```json
{
  "predicted_ac_power": 12345.678,
  "unit": "kW",
  "timestamp": "2020-06-15T12:00:00"
}
```

### Core service responsibilities

1. Validate incoming sensor/weather data using Pydantic.
2. Extract time-based features from `date_time`.
3. Build the same feature schema used during training.
4. Load the trained XGBoost model once when the API starts.
5. Run inference through `/predict`.
6. Return a JSON response suitable for a frontend/dashboard.
7. Expose `/health` for deployment monitoring and `/model-info` for model metadata.

## Important unit note

The supplied dataset's `AC_POWER` values are typically in the dataset's power unit, commonly treated as kW in this project. Verify the plant's actual instrumentation/unit definition before presenting the value as a physical kW measurement in a production dashboard.

## Next backend extensions

- `/predict/batch` for multiple timestamps.
- `/forecast/day` for day-ahead forecasting.
- PostgreSQL/TimescaleDB for sensor history.
- `/faults/detect` for the second project module.
- Background jobs for periodic prediction.
- Authentication and rate limiting before production deployment.
