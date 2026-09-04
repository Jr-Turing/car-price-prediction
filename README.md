# 🚗 Car Price Prediction API

<p align="center">
  <img src="assets/car-price.png" alt="Car Price Prediction" width="100%">
</p>

<p align="center">
  <strong>Machine Learning powered used car price prediction API built with FastAPI and RandomForest.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-API-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/Scikit--learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-learn">
  <img src="https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/uv-Package_Manager-6E56CF?style=for-the-badge&logo=uv&logoColor=white" alt="uv">
</p>

---

## 📌 Overview

**Car Price Prediction API** is a machine learning project that predicts the
selling price of a used car based on its characteristics.

The project provides:

- A **RandomForest regression model** for price prediction.
- A **FastAPI backend** exposing the ML model through a REST API.
- A **Streamlit frontend** for easy interaction with the prediction API.
- A model training pipeline for retraining the model using the dataset.
- Proper feature alignment between training and inference.
- Modern Python dependency management using **uv**.

The project is designed with a clean and modular structure so that the
machine learning model can be easily trained, tested, and served through an API.

---

## ✨ Features

- 🤖 **RandomForest Regression** for used car price prediction
- ⚡ **FastAPI** REST API
- 🎨 **Streamlit** interactive frontend
- 📊 Used car price prediction
- 🧠 Automated preprocessing
- 🔤 One-hot encoding for categorical features
- 📐 Consistent feature ordering during inference
- 🔄 Model retraining support
- 🧩 Pydantic request and response validation
- 📦 Modern Python packaging with `pyproject.toml`
- ⚡ Fast dependency management with `uv`
- 📁 Clean and modular project structure

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python** | Programming language |
| **FastAPI** | Backend REST API |
| **Scikit-learn** | Machine Learning |
| **RandomForest** | Regression model |
| **Pydantic** | Request/response validation |
| **Streamlit** | Interactive frontend |
| **uv** | Python package and dependency management |
| **Pickle** | Model artifact storage |

---

## 🏗️ Project Structure

```text
car-price-api/
│
├── assets/
│   └── car-price-prediction.png
│
├── data/
│   └── cardekho_data.csv
│
├── models/
│   ├── random_forest_model.pkl
│   └── feature_columns.pkl
│
├── src/
│   └── car_price_api/
│       ├── __init__.py
│       ├── main.py
│       ├── model.py
│       ├── schema.py
│       ├── train.py
│       └── streamlit_app.py
│
├── .gitignore
├── pyproject.toml
├── uv.lock
└── README.md
```

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/car-price-api.git
cd car-price-api
```

### 2. Install dependencies with uv

```bash
uv sync
```

This creates a `.venv` and installs everything from `pyproject.toml` / `uv.lock`.

### 3. Run the API

```bash
uv run uvicorn car_price_api.main:app --reload
```

- Health check: `GET http://127.0.0.1:8000/`
- Interactive docs: `http://127.0.0.1:8000/docs`

### 4. Run the Streamlit UI

In a second terminal (with the API already running):

```bash
uv run streamlit run src/car_price_api/streamlit_app.py
```

### 5. Retrain the model (optional)

```bash
uv run python -m car_price_api.train
```

---

## 📡 API Usage

**Endpoint:** `POST /predict`

**Request body:**

```json
{
  "Car_Name": "ritz",
  "Year": 2014,
  "Present_Price": 5.59,
  "Kms_Driven": 27000,
  "Fuel_Type": "Petrol",
  "Seller_Type": "Dealer",
  "Transmission": "Manual",
  "Owner": 0
}
```

**Example with curl:**

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
        "Car_Name": "ritz",
        "Year": 2014,
        "Present_Price": 5.59,
        "Kms_Driven": 27000,
        "Fuel_Type": "Petrol",
        "Seller_Type": "Dealer",
        "Transmission": "Manual",
        "Owner": 0
      }'
```

**Response:**

```json
{
  "prediction_price": 3.81
}
```

---

## 🧠 How It Works

1. The RandomForest model is trained on the CarDekho used car dataset (`train.py`).
2. Categorical features (`Fuel_Type`, `Seller_Type`, `Transmission`, `Owner`, `Car_Name`) are one-hot encoded.
3. The exact training column order is saved to `feature_columns.pkl` so inference always matches training.
4. At inference time, incoming requests are preprocessed the same way and aligned to those columns before prediction.

---

<p align="center">
  Made with ❤️ by <strong>Curious Arvind</strong> using FastAPI, RandomForest, and uv.
</p>