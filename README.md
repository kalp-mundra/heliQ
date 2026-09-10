# 🌞 Heliq

### AI-Based Solar Panel Energy Output Prediction and Fault Detection System

**Heliq** is an AI-powered solar panel monitoring system designed to predict solar energy output and detect performance abnormalities in photovoltaic (PV) panels.

The system analyzes solar panel performance and environmental parameters using **Machine Learning, anomaly detection, and rule-based techniques** to identify potential issues such as **dust accumulation, partial shading, hotspots, and electrical abnormalities**.

Heliq provides performance predictions, anomaly insights, and fault alerts through an interactive and responsive dashboard.

---

## 🚀 Features

* ⚡ **Solar Energy Output Prediction**
* 🔍 **AI-Based Fault & Anomaly Detection**
* 🤖 **Isolation Forest-Based Anomaly Detection**
* 📊 **Rule-Based Fault Detection**
* 📈 **Interactive Solar Performance Dashboard**
* 🚨 **Fault & Anomaly Alerts**
* 🗄️ **PostgreSQL-Based Data Storage**
* 🔗 **FastAPI Backend for ML & Data Services**
* 📱 **Responsive React-Based Interface**
* 📊 **Solar Performance Monitoring & Visualization**

---

## 🧠 Machine Learning

Heliq combines Machine Learning and rule-based techniques to analyze solar panel performance and identify abnormal behavior.

### Techniques Used

#### 1. Energy Output Prediction

The system predicts the expected energy generation of a solar panel using relevant environmental and panel performance parameters.

Potential input parameters include:

* Solar irradiance
* Temperature
* Panel voltage
* Panel current
* Historical energy generation
* Environmental conditions
* Other relevant PV system parameters

The predicted output can be compared with actual generation to identify performance degradation.

---

#### 2. Isolation Forest

**Isolation Forest** is used for unsupervised anomaly detection.

It identifies observations that significantly differ from normal solar panel operating behavior.

This can help detect conditions such as:

* ⚠️ Unexpected performance drops
* 🌫️ Dust accumulation
* 🌥️ Partial shading
* 🔥 Potential hotspots
* ⚡ Electrical abnormalities
* 📉 Unusual energy generation patterns

---

#### 3. Rule-Based Fault Detection

In addition to Machine Learning, Heliq uses predefined rules based on solar panel operating conditions.

For example:

```text
If expected_output >> actual_output
        ↓
Potential performance degradation

If voltage/current behavior is abnormal
        ↓
Potential electrical fault

If panel output drops significantly under suitable irradiance
        ↓
Potential shading or dust accumulation
```

Combining ML-based anomaly detection with domain-based rules provides a more interpretable fault detection system.

---

## 🏗️ System Architecture

```text
                    Solar Panel Data
                           │
                           ▼
                 Data Preprocessing
                           │
                           ▼
                 Feature Engineering
                           │
                           ▼
                ┌─────────────────────┐
                │   ML & Detection    │
                │      Layer          │
                └─────────────────────┘
                    │             │
          ┌─────────┘             └─────────┐
          ▼                                 ▼
  Energy Prediction                Fault Detection
          │                                 │
          │                         ┌───────┴────────┐
          │                         │                │
          │                    Isolation Forest   Rule-Based
          │                         │                │
          └──────────────┬──────────┴────────────────┘
                         ▼
                     FastAPI
                         │
                         ▼
                    PostgreSQL
                         │
                         ▼
              React + Tailwind CSS
                    Dashboard
                         │
                         ▼
          Performance Insights & Alerts
```

---

## 🛠️ Technology Stack

### Frontend

* **React**
* **Tailwind CSS**
* **Recharts**

Used to build the interactive and responsive solar monitoring dashboard.

### Backend

* **Python**
* **FastAPI**

FastAPI provides APIs for:

* Energy prediction
* Fault detection
* Anomaly detection
* Solar performance data
* Dashboard services

### Database

* **PostgreSQL**

Used for storing:

* Solar panel data
* Environmental parameters
* Prediction results
* Anomaly detection results
* Fault information
* Historical performance data

### Machine Learning

* **Python**
* **Scikit-learn**
* **Isolation Forest**
* **Rule-Based Detection**
* **Feature Engineering**
* **Regression-based Energy Prediction**

---

## 📊 Dashboard

The Heliq dashboard is designed to provide a centralized view of solar panel performance.

### Dashboard Capabilities

* ⚡ Current energy output
* 📈 Historical energy generation
* 🔮 Predicted energy output
* 🔍 Anomaly status
* 🚨 Fault alerts
* 🌡️ Environmental parameters
* 📊 Performance trends
* 🟢 Normal / 🔴 Abnormal operating status

---

## 🔄 How Heliq Works

### Step 1 — Data Collection

Solar panel and environmental data is collected from the available dataset or connected monitoring system.

```text
Panel Sensors
     +
Environmental Data
     ↓
Solar Panel Dataset
```

### Step 2 — Data Preprocessing

Raw data is cleaned and prepared for Machine Learning.

Operations may include:

* Missing-value handling
* Data cleaning
* Feature selection
* Feature scaling
* Outlier analysis
* Feature engineering

### Step 3 — Energy Prediction

The prediction model estimates the expected solar energy output.

```text
Panel + Environmental Parameters
              ↓
       Prediction Model
              ↓
      Expected Energy Output
```

### Step 4 — Anomaly Detection

The system compares the observed behavior against learned normal operating patterns using Isolation Forest.

```text
Solar Performance Data
          ↓
    Isolation Forest
          ↓
   Normal / Anomaly
```

### Step 5 — Fault Detection

Rule-based logic analyzes important operating conditions to identify potential faults.

```text
Sensor Parameters
       ↓
Fault Rules
       ↓
Potential Fault
```

### Step 6 — API Layer

The FastAPI backend connects the Machine Learning models, database, and frontend.

```text
React Dashboard
       ↕
    FastAPI
       ↕
 ML Models + PostgreSQL
```

### Step 7 — Visualization

The React dashboard presents predictions, anomalies, performance trends, and alerts to the user.

---

## 📁 Project Structure

```text
Heliq/
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── ...
│
├── backend/
│   ├── app/
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── main.py
│   └── requirements.txt
│
├── ml/
│   ├── data/
│   ├── notebooks/
│   ├── preprocessing/
│   ├── training/
│   ├── prediction/
│   └── anomaly_detection/
│
├── database/
│   ├── schemas/
│   └── migrations/
│
├── .gitignore
├── README.md
└── LICENSE
```

> The project structure may evolve as development progresses.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/heliq.git
cd heliq
```

---

### 2. Backend Setup

Create a virtual environment:

```bash
python -m venv venv
```

Activate it.

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r backend/requirements.txt
```

Start the FastAPI server:

```bash
uvicorn backend.main:app --reload
```

The backend will be available at:

```text
http://localhost:8000
```

API documentation:

```text
http://localhost:8000/docs
```

---

### 3. Frontend Setup

Navigate to the frontend:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

The frontend will be available at the URL displayed by the development server.

---

## 🗄️ Database Setup

Heliq uses **PostgreSQL** for persistent storage.

Create a PostgreSQL database and configure the database connection through environment variables.

Example:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/heliq
```

> Do not commit `.env` files or database credentials to GitHub.

---

## 🔐 Environment Variables

Create a `.env` file for environment-specific configuration.

Example:

```env
DATABASE_URL=your_postgresql_connection_string
```

Additional variables can be added as the project evolves.

Make sure `.env` is included in `.gitignore`.

---

## 🧪 Machine Learning Pipeline

```text
Raw Solar Data
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
Train / Validation Split
      │
      ├─────────────────────┐
      ▼                     ▼
Energy Prediction     Anomaly Detection
      │                     │
      ▼                     ▼
Expected Output       Anomaly Score
      │                     │
      └──────────┬──────────┘
                 ▼
          Fault Analysis
                 │
                 ▼
        Prediction + Alert
```

---

## 🎯 Fault Detection

Heliq aims to identify abnormal operating conditions including:

| Condition                 | Possible Effect                  |
| ------------------------- | -------------------------------- |
| 🌫️ Dust Accumulation     | Reduced energy output            |
| 🌥️ Partial Shading       | Uneven/reduced generation        |
| 🔥 Hotspots               | Potential panel damage           |
| ⚡ Electrical Abnormality  | Voltage/current irregularities   |
| 📉 Unexpected Output Drop | Possible performance degradation |
| 🚨 Anomalous Behavior     | Requires further inspection      |

> Fault classification depends on the available sensor data and detection rules implemented in the system.

---

## 📈 Future Improvements

Planned improvements may include:

* 🔮 More accurate energy forecasting models
* 📡 Real-time IoT sensor integration
* 🌐 Remote solar plant monitoring
* 🧠 Advanced deep learning models
* 🔥 Dedicated hotspot detection
* 📸 Computer vision-based panel inspection
* 📊 Advanced analytics and reporting
* 🔔 Email/SMS/notification-based alerts
* 👥 User authentication and role-based access
* ☁️ Cloud deployment
* 📱 Mobile-friendly monitoring experience

---

## 👥 Team

Heliq is developed as a collaborative project by a team of four developers.

| Member            | Responsibility                       |
| ----------------- | ------------------------------------ |
| **Team Member 1** | Machine Learning / Energy Prediction |
| **Team Member 2** | Anomaly & Fault Detection            |
| **Team Member 3** | Backend / Database                   |
| **Team Member 4** | Frontend / Dashboard                 |

> Update the names and responsibilities as your team finalizes the division of work.

---

## 🤝 Contributing

We use a feature-branch workflow for collaborative development.

### Create a branch

```bash
git checkout -b feature/your-feature
```

### Make your changes

```bash
git add .
git commit -m "Add your feature"
```

### Push your branch

```bash
git push -u origin feature/your-feature
```

Then create a **Pull Request** on GitHub.

### Recommended workflow

```text
main
 │
 ├── feature/energy-prediction
 │
 ├── feature/anomaly-detection
 │
 ├── feature/backend-api
 │
 └── feature/dashboard
```

Pull Requests should be reviewed before being merged into `main`.

---

## 📜 License

This project is currently developed for educational and project purposes.

A formal open-source license can be added when the project is ready for public release.

---

## 🌞 Heliq

**Turning solar data into actionable intelligence.**

> Predict. Detect. Monitor. Optimize.
