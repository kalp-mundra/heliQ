import json
from pathlib import Path
import joblib
import pandas as pd
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

GEN_PATH = "data/Plant_1_Generation_Data.csv"
WEATHER_PATH = "data/Plant_1_Weather_Sensor_Data.csv"
MODEL_DIR = Path("models")
MODEL_DIR.mkdir(exist_ok=True)

gen = pd.read_csv(GEN_PATH)
weather = pd.read_csv(WEATHER_PATH)

gen["DATE_TIME"] = pd.to_datetime(gen["DATE_TIME"], format="%d-%m-%Y %H:%M")
weather["DATE_TIME"] = pd.to_datetime(weather["DATE_TIME"])

generation = (
    gen.groupby(["DATE_TIME", "PLANT_ID"], as_index=False)
       .agg(AC_POWER=("AC_POWER", "sum"))
)

weather = weather.drop_duplicates(["DATE_TIME", "PLANT_ID"])
df = generation.merge(weather, on=["DATE_TIME", "PLANT_ID"], how="inner")

df["hour"] = df["DATE_TIME"].dt.hour + df["DATE_TIME"].dt.minute / 60.0
df["day_of_year"] = df["DATE_TIME"].dt.dayofyear
df["month"] = df["DATE_TIME"].dt.month
df["day_of_week"] = df["DATE_TIME"].dt.dayofweek
df["is_daylight"] = (df["IRRADIATION"] > 0).astype(int)

features = [
    "AMBIENT_TEMPERATURE", "MODULE_TEMPERATURE", "IRRADIATION",
    "hour", "day_of_year", "month", "day_of_week", "is_daylight"
]
target = "AC_POWER"

df = df.dropna(subset=features + [target]).sort_values("DATE_TIME")
split = int(len(df) * 0.80)

train_df = df.iloc[:split]
test_df = df.iloc[split:]

model = XGBRegressor(
    n_estimators=500, max_depth=8, learning_rate=0.05,
    subsample=0.9, colsample_bytree=0.9,
    objective="reg:squarederror", random_state=42, n_jobs=4
)
model.fit(train_df[features], train_df[target])

pred = model.predict(test_df[features])
metadata = {
    "features": features,
    "target": target,
    "mae": float(mean_absolute_error(test_df[target], pred)),
    "rmse": float(mean_squared_error(test_df[target], pred) ** 0.5),
    "r2": float(r2_score(test_df[target], pred)),
}

joblib.dump(model, MODEL_DIR / "ac_power_xgb.joblib")
with open(MODEL_DIR / "metadata.json", "w") as f:
    json.dump(metadata, f, indent=2)

print(json.dumps(metadata, indent=2))
