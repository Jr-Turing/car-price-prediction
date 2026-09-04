from pathlib import Path

import joblib
import pandas as pd

# src/car_price_api/model.py -> project root is two levels up
PROJECT_ROOT = Path(__file__).resolve().parents[2]
MODEL_PATH = PROJECT_ROOT / "models" / "random_forest_model.pkl"
COLS_PATH = PROJECT_ROOT / "models" / "feature_columns.pkl"

_model = None
_feature_columns = None


def load_artifacts() -> None:
    global _model, _feature_columns
    if _model is None:
        _model = joblib.load(MODEL_PATH)
    if _feature_columns is None:
        _feature_columns = joblib.load(COLS_PATH)


def preprocess(payload: dict) -> pd.DataFrame:
    """
    Converts raw input into the SAME one-hot encoded column structure used in training.
    """
    if _feature_columns is None:
        raise RuntimeError("Artifacts not loaded. Call load_artifacts() first.")

    df = pd.DataFrame([payload])

    categorical_cols = ["Fuel_Type", "Seller_Type", "Transmission", "Owner", "Car_Name"]
    df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

    # Add any training columns missing from this single-row encoding, all at once
    missing_cols = [c for c in _feature_columns if c not in df_encoded.columns]
    if missing_cols:
        missing_df = pd.DataFrame(0, index=df_encoded.index, columns=missing_cols)
        df_encoded = pd.concat([df_encoded, missing_df], axis=1)

    # Keep only the training columns, in the exact training order
    return df_encoded[_feature_columns]


def predict_price(payload: dict) -> float:
    load_artifacts()
    X = preprocess(payload)
    pred = _model.predict(X)[0]
    return float(pred)
