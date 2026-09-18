import pandas as pd
import os

GENERATION_FILE = "data/Plant_1_Generation_Data.csv"
WEATHER_FILE = "data/Plant_1_Weather_Sensor_Data.csv"
OUTPUT_FILE = "data/solar_combined_data.csv"

def load_generation_data():
    print("Loading solar generation data...")
    generation = pd.read_csv(GENERATION_FILE)
    print("Generation Data Shape:", generation.shape)
    print("\nGeneration Columns:")
    print(generation.columns.tolist())
    generation["DATE_TIME"] = pd.to_datetime(
        generation["DATE_TIME"], format="%d-%m-%Y %H:%M", errors="coerce"
    )
    return generation

def load_weather_data():
    print("\nLoading weather sensor data...")
    weather = pd.read_csv(WEATHER_FILE)
    print("Weather Data Shape:", weather.shape)
    print("\nWeather Columns:")
    print(weather.columns.tolist())
    weather["DATE_TIME"] = pd.to_datetime(weather["DATE_TIME"], errors="coerce")
    return weather

def clean_generation_data(generation):
    generation = generation.drop_duplicates()
    generation = generation.dropna(subset=["DATE_TIME"])
    for column in ["DC_POWER", "AC_POWER", "DAILY_YIELD", "TOTAL_YIELD"]:
        if column in generation.columns:
            generation[column] = generation[column].fillna(0)
    return generation

def clean_weather_data(weather):
    weather = weather.drop_duplicates()
    weather = weather.dropna(subset=["DATE_TIME"])
    for column in ["AMBIENT_TEMPERATURE", "MODULE_TEMPERATURE", "IRRADIATION"]:
        if column in weather.columns:
            weather[column] = weather[column].interpolate()
    return weather

def aggregate_generation(generation):
    print("\nAggregating inverter-level generation data...")
    return (
        generation.groupby(["DATE_TIME", "PLANT_ID"], as_index=False)
        .agg({
            "DC_POWER": "sum",
            "AC_POWER": "sum",
            "DAILY_YIELD": "sum",
            "TOTAL_YIELD": "sum"
        })
    )

def merge_datasets(generation, weather):
    weather = weather.drop_duplicates(subset=["DATE_TIME", "PLANT_ID"])
    return pd.merge(
        generation, weather,
        on=["DATE_TIME", "PLANT_ID"],
        how="inner"
    )

def create_time_features(data):
    data["hour"] = data["DATE_TIME"].dt.hour + data["DATE_TIME"].dt.minute / 60
    data["day"] = data["DATE_TIME"].dt.day
    data["month"] = data["DATE_TIME"].dt.month
    data["day_of_year"] = data["DATE_TIME"].dt.dayofyear
    data["day_of_week"] = data["DATE_TIME"].dt.dayofweek
    data["is_daylight"] = (data["IRRADIATION"] > 0).astype(int)
    return data

def collect_data():
    generation = load_generation_data()
    weather = load_weather_data()

    generation = clean_generation_data(generation)
    weather = clean_weather_data(weather)
    generation = aggregate_generation(generation)

    combined = merge_datasets(generation, weather)
    combined = create_time_features(combined)
    combined = combined.sort_values("DATE_TIME")

    os.makedirs("data", exist_ok=True)
    combined.to_csv(OUTPUT_FILE, index=False)

    print("\nDATA COLLECTION COMPLETED")
    print("Final Dataset Shape:", combined.shape)
    print("Saved to:", OUTPUT_FILE)
    print("\nFirst 5 records:")
    print(combined.head())

    return combined

if __name__ == "__main__":
    collect_data()
