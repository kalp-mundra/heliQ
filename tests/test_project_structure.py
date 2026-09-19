from pathlib import Path


def test_project_structure():
    required_directories = [
        "dataset",
        "dataset/energy_prediction",
        "dataset/fault_detection",
        "ml",
        "ml/preprocessing",
        "ml/training",
        "ml/anomaly_detection",
        "backend",
        "frontend",
        "tests",
    ]

    for directory in required_directories:
        assert Path(directory).is_dir(), f"Missing directory: {directory}"