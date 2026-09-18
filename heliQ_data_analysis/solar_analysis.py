import pandas as pd
import matplotlib.pyplot as plt
import os

DATA_FILE = "data/solar_combined_data.csv"
OUTPUT_DIR = "analysis_results"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def load_data():
    return pd.read_csv(DATA_FILE, parse_dates=["DATE_TIME"])

def basic_analysis(data):
    print("\n========== BASIC SOLAR DATA ANALYSIS ==========")
    print("\nDataset Shape:", data.shape)
    print("\nColumns:")
    print(data.columns.tolist())
    print("\nMissing Values:")
    print(data.isnull().sum())
    print("\nStatistical Summary:")
    print(data[[
        "AC_POWER", "DC_POWER", "DAILY_YIELD",
        "AMBIENT_TEMPERATURE", "MODULE_TEMPERATURE", "IRRADIATION"
    ]].describe())

def irradiation_analysis(data):
    plt.figure(figsize=(10, 6))
    plt.scatter(data["IRRADIATION"], data["AC_POWER"], alpha=0.25)
    plt.xlabel("Solar Irradiation")
    plt.ylabel("AC Power")
    plt.title("Solar Irradiation vs AC Power")
    plt.grid(True)
    plt.savefig(f"{OUTPUT_DIR}/irradiation_vs_power.png", dpi=300, bbox_inches="tight")
    plt.show()

def hourly_analysis(data):
    hourly = data.groupby("hour")["AC_POWER"].mean()
    print("\nAverage AC Power by Hour:")
    print(hourly)
    plt.figure(figsize=(10, 6))
    hourly.plot()
    plt.xlabel("Hour of Day")
    plt.ylabel("Average AC Power")
    plt.title("Average Solar Power by Hour")
    plt.grid(True)
    plt.savefig(f"{OUTPUT_DIR}/hourly_power_pattern.png", dpi=300, bbox_inches="tight")
    plt.show()

def hourly_irradiation(data):
    hourly = data.groupby("hour")["IRRADIATION"].mean()
    plt.figure(figsize=(10, 6))
    hourly.plot()
    plt.xlabel("Hour of Day")
    plt.ylabel("Average Irradiation")
    plt.title("Average Solar Irradiation by Hour")
    plt.grid(True)
    plt.savefig(f"{OUTPUT_DIR}/hourly_irradiation.png", dpi=300, bbox_inches="tight")
    plt.show()

def temperature_analysis(data):
    plt.figure(figsize=(10, 6))
    plt.scatter(data["MODULE_TEMPERATURE"], data["AC_POWER"], alpha=0.25)
    plt.xlabel("Module Temperature")
    plt.ylabel("AC Power")
    plt.title("Module Temperature vs AC Power")
    plt.grid(True)
    plt.savefig(f"{OUTPUT_DIR}/temperature_vs_power.png", dpi=300, bbox_inches="tight")
    plt.show()

def monthly_analysis(data):
    monthly = data.groupby("month")["AC_POWER"].mean()
    print("\nAverage AC Power by Month:")
    print(monthly)
    plt.figure(figsize=(10, 6))
    monthly.plot(kind="bar")
    plt.xlabel("Month")
    plt.ylabel("Average AC Power")
    plt.title("Average Solar Power by Month")
    plt.grid(axis="y")
    plt.savefig(f"{OUTPUT_DIR}/monthly_power_pattern.png", dpi=300, bbox_inches="tight")
    plt.show()

def daily_analysis(data):
    daily = data.groupby(data["DATE_TIME"].dt.date)["AC_POWER"].sum()
    print("\nDaily production statistics:")
    print(daily.describe())
    plt.figure(figsize=(12, 6))
    daily.plot()
    plt.xlabel("Date")
    plt.ylabel("Total AC Power")
    plt.title("Daily Solar Energy Production")
    plt.grid(True)
    plt.savefig(f"{OUTPUT_DIR}/daily_energy_pattern.png", dpi=300, bbox_inches="tight")
    plt.show()

def correlation_analysis(data):
    columns = [
        "AC_POWER", "DC_POWER", "AMBIENT_TEMPERATURE",
        "MODULE_TEMPERATURE", "IRRADIATION"
    ]
    correlation = data[columns].corr()
    print("\n========== CORRELATION ANALYSIS ==========")
    print(correlation)
    correlation.to_csv(f"{OUTPUT_DIR}/correlation_matrix.csv")

def peak_generation(data):
    peak = data.loc[data["AC_POWER"].idxmax()]
    print("\n========== PEAK SOLAR GENERATION ==========")
    print("Maximum AC Power:", peak["AC_POWER"])
    print("Timestamp:", peak["DATE_TIME"])
    print("Irradiation:", peak["IRRADIATION"])
    print("Module Temperature:", peak["MODULE_TEMPERATURE"])

def analyse_solar_patterns():
    data = load_data()
    basic_analysis(data)
    irradiation_analysis(data)
    hourly_analysis(data)
    hourly_irradiation(data)
    temperature_analysis(data)
    monthly_analysis(data)
    daily_analysis(data)
    correlation_analysis(data)
    peak_generation(data)

if __name__ == "__main__":
    analyse_solar_patterns()
