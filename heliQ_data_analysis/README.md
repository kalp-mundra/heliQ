# Heliq - Solar Data Collection & Pattern Analysis

## Tasks covered

1. Collect solar panel performance data
2. Analyse solar energy patterns

## Folder structure

```text
heliq_data_collection_analysis/
├── data/
│   ├── Plant_1_Generation_Data.csv
│   └── Plant_1_Weather_Sensor_Data.csv
├── analysis_results/
├── data_collection.py
├── solar_analysis.py
├── requirements.txt
└── README.md
```

## Setup

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Step 1: Collect and preprocess data

```bash
python data_collection.py
```

This creates:

```text
data/solar_combined_data.csv
```

The script:
- loads generation and weather data
- parses timestamps
- removes duplicates
- handles missing values
- aggregates 22 inverter readings into plant-level values
- merges generation and weather data
- creates time features

## Step 2: Analyse solar patterns

```bash
python solar_analysis.py
```

Generated files:

```text
analysis_results/
├── irradiation_vs_power.png
├── hourly_power_pattern.png
├── hourly_irradiation.png
├── temperature_vs_power.png
├── monthly_power_pattern.png
├── daily_energy_pattern.png
└── correlation_matrix.csv
```

These analyses are directly useful for the later energy-output prediction and fault-detection modules.
