import pandas as pd


def test_plant1_generation_dataset():
    df = pd.read_csv(
        "dataset/energy_prediction/Plant_1_Generation_Data.csv"
    )

    assert len(df) > 0
    assert "DC_POWER" in df.columns
    assert "AC_POWER" in df.columns


def test_plant1_weather_dataset():
    df = pd.read_csv(
        "dataset/energy_prediction/Plant_1_Weather_Sensor_Data.csv"
    )

    assert len(df) > 0
    assert "IRRADIATION" in df.columns
    assert "AMBIENT_TEMPERATURE" in df.columns


def test_plant2_generation_dataset():
    df = pd.read_csv(
        "dataset/energy_prediction/Plant_2_Generation_Data.csv"
    )

    assert len(df) > 0
    assert "DC_POWER" in df.columns
    assert "AC_POWER" in df.columns


def test_fault_detection_dataset():
    df = pd.read_csv(
        "dataset/fault_detection/train_data.csv",
        sep=";"
    )

    assert len(df) > 0
    assert "class" in df.columns


def test_plant1_generation_no_missing_values():
    df = pd.read_csv(
        "dataset/energy_prediction/Plant_1_Generation_Data.csv"
    )

    assert df.isnull().sum().sum() == 0


def test_fault_detection_no_missing_values():
    df = pd.read_csv(
        "dataset/fault_detection/train_data.csv",
        sep=";"
    )

    assert df.isnull().sum().sum() == 0


def test_generation_numeric_columns():
    df = pd.read_csv(
        "dataset/energy_prediction/Plant_1_Generation_Data.csv"
    )

    numeric_columns = [
        "DC_POWER",
        "AC_POWER",
        "DAILY_YIELD",
        "TOTAL_YIELD"
    ]

    for column in numeric_columns:
        assert pd.api.types.is_numeric_dtype(df[column])
