import os

import requests
import streamlit as st

st.set_page_config(page_title="Car Price Prediction", page_icon="🚗", layout="centered")

API_URL = os.getenv("API_URL", "http://127.0.0.1:8000/predict")

st.title("🚗 Car Price Prediction")
st.caption(
    "This UI sends data to your FastAPI backend and shows predicted selling price."
)

# --- Inputs (match your dataset columns exactly) ---
car_name = st.text_input("Car_Name (e.g. swift, ritz, sx4)", value="swift")

year = st.number_input("Year", min_value=1990, max_value=2026, value=2014, step=1)

present_price = st.number_input(
    "Present_Price (in lakhs)", min_value=0.0, value=5.59, step=0.1
)

kms_driven = st.number_input("Kms_Driven", min_value=0, value=40000, step=1000)

fuel_type = st.selectbox("Fuel_Type", ["Petrol", "Diesel", "CNG"])

seller_type = st.selectbox("Seller_Type", ["Dealer", "Individual"])

transmission = st.selectbox("Transmission", ["Manual", "Automatic"])

# Owner is numeric in your dataset (0,1,3). Map UI labels to int.
owner_label = st.selectbox(
    "Owner", ["0 (First Owner)", "1 (Second Owner)", "3 (Third Owner)"]
)
owner = int(owner_label.split()[0])

payload = {
    "Car_Name": str(car_name),
    "Year": int(year),
    "Present_Price": float(present_price),
    "Kms_Driven": int(kms_driven),
    "Fuel_Type": str(fuel_type),
    "Seller_Type": str(seller_type),
    "Transmission": str(transmission),
    "Owner": int(owner),
}

st.write("### Payload being sent:")
st.json(payload)

if st.button("Predict Price 💰"):
    try:
        res = requests.post(API_URL, json=payload, timeout=20)
        if res.status_code == 200:
            data = res.json()
            pred = data.get("prediction_price")

            if pred is None:
                st.warning(
                    "API responded but prediction key not found. Full response below:"
                )
                st.json(data)
            else:
                st.success(f"✅ Predicted Selling Price: **₹ {pred:.2f} lakhs**")
        else:
            st.error(f"❌ API Error {res.status_code}")
            st.code(res.text)
    except requests.exceptions.RequestException as e:
        st.error("❌ Could not connect to API. Is FastAPI running?")
        st.code(str(e))
