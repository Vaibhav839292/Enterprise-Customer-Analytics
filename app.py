import streamlit as st
import pickle
import numpy as np
import requests
import os

# Google Drive Direct Links
MODEL_URL = 'https://docs.google.com/uc?export=download&id=1SijgUq256_1fjz5ylxODdQyM6T138GMU'
SCALER_URL = 'https://docs.google.com/uc?export=download&id=1hTOLjDhHtCRCdNYB4-ObCB78Ox0WvfeN'

# File download function
def download_file(url, filename):
    response = requests.get(url, allow_redirects=True)
    with open(filename, 'wb') as f:
        f.write(response.content)

# Files download karo
if not os.path.exists('churn_model.pkl'):
    download_file(MODEL_URL, 'churn_model.pkl')
if not os.path.exists('scaler.pkl'):
    download_file(SCALER_URL, 'scaler.pkl')

# Load model using pickle (Ye line important hai!)
with open('churn_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

st.title("Bank Customer Churn Predictor")

# Input fields
age = st.number_input("Age", 18, 100)
balance = st.number_input("Balance", 0, 500000)

if st.button("Predict"):
    input_data = np.array([[age, balance]])
    
    # Scaling
    input_data_scaled = scaler.transform(input_data)
    
    # Prediction
    prediction = model.predict(input_data_scaled)
    
    if prediction[0] == 1:
        st.write("Customer will Churn.")
    else:
        st.write("Customer will not Churn.")
