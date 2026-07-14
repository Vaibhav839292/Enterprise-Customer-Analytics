import streamlit as st
import joblib
import numpy as np
import gdown
import os

# Google Drive File IDs (Sirf ID daalni hai)
MODEL_ID = '1SijgUq256_1fjz5ylxODdQyM6T138GMU'
SCALER_ID = '1hTOLjDhHtCRCdNYB4-ObCB78Ox0WvfeN'

# Download function
if not os.path.exists('churn_model.pkl'):
    gdown.download(id=MODEL_ID, output='churn_model.pkl', quiet=False)
if not os.path.exists('scaler.pkl'):
    gdown.download(id=SCALER_ID, output='scaler.pkl', quiet=False)

# Load model
model = joblib.load('churn_model.pkl')
scaler = joblib.load('scaler.pkl')

st.title("Bank Customer Churn Predictor")
age = st.number_input("Age", 18, 100)
balance = st.number_input("Balance", 0, 500000)

if st.button("Predict"):
    input_data = np.array([[age, balance]])
    input_data_scaled = scaler.transform(input_data)
    prediction = model.predict(input_data_scaled)
    if prediction[0] == 1:
        st.write("Customer will Churn.")
    else:
        st.write("Customer will not Churn.")
