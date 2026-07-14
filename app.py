import streamlit as st
import joblib
import numpy as np
import requests
import os

st.write("Checking files...")

MODEL_URL = 'https://docs.google.com/uc?export=download&id=1_nqlIDoKTWsmEJPL6OwP5mnDOLZ3dwlf'
SCALER_URL = 'https://docs.google.com/uc?export=download&id=17eH1mLEwnm5-ptDLuRp9EvqJo2KP5LVp'

def download_file(url, filename):
    st.write(f"Downloading {filename}...")
    response = requests.get(url, allow_redirects=True)
    with open(filename, 'wb') as f:
        f.write(response.content)
    st.write(f"Done downloading {filename}")

if not os.path.exists('churn_model.pkl'):
    download_file(MODEL_URL, 'churn_model.pkl')

if not os.path.exists('scaler.pkl'):
    download_file(SCALER_URL, 'scaler.pkl')

st.write("Loading model...")
model = joblib.load('churn_model.pkl')
scaler = joblib.load('scaler.pkl')
st.write("Model loaded successfully!")

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
