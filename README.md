# Car Price Prediction API

A FastAPI service that predicts a used car's selling price with a
RandomForest model, plus a small Streamlit UI that calls it.

## Project structure

```
car-price-api/
├── pyproject.toml           # package + dependency config
├── README.md
├── data/
│   └── cardekho_data.csv    # training data
├── models/
│   ├── random_forest_model.pkl   # trained model
│   └── feature_columns.pkl       # training column order (for inference alignment)
└── src/
    └── car_price_api/
        ├── __init__.py
        ├── main.py           # FastAPI app (/, /predict)
        ├── model.py          # loads artifacts, preprocesses input, predicts
        ├── schema.py         # pydantic request/response models
        ├── train.py          # retrains the model from data/cardekho_data.csv
        └── streamlit_app.py  # Streamlit front end
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -e .
```

## Run the API

```bash
uvicorn car_price_api.main:app --reload
```

- `GET /` → health check
- `POST /predict` → body matches `CarFeatures` in `schema.py`, returns `{"prediction_price": <float>}`
- Interactive docs: http://127.0.0.1:8000/docs

## Run the Streamlit UI

In a second terminal (with the API already running):

```bash
streamlit run src/car_price_api/streamlit_app.py
```

Set `API_URL` if the API isn't on the default `http://127.0.0.1:8000/predict`.

## Retrain the model

```bash
python -m car_price_api.train
```

This reads `data/cardekho_data.csv` and overwrites the files in `models/`.

## Notes

- `Car_Name` and `Owner` are one-hot encoded the same way during training and
  inference (`feature_columns.pkl` records the exact training column order).
  Car names not seen during training simply fall back to all-zero indicator
  columns for that name.
