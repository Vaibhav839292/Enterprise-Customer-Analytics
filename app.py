import streamlit as st
import joblib
import numpy as np
import requests
import os

# Google Drive Direct Links
MODEL_URL = 'https://docs.google.com/uc?export=download&id=1_nqlIDoKTWsmEJPL6OwP5mnDOLZ3dwlf'
SCALER_URL = 'https://docs.google.com/uc?export=download&id=17eH1mLEwnm5-ptDLuRp9EvqJo2KP5LVp'

# File download function
def download_file(url, filename):
    # Agar file pehle se wahan hai, toh use hata do
    if os.path.exists(filename):
        os.remove(filename)
    
    response = requests.get(url, allow_redirects=True)
    with open(filename, 'wb') as f:
        f.write(response.content)

# Files download karo
download_file(MODEL_URL, 'churn_model.pkl')
download_file(SCALER_URL, 'scaler.pkl')

# Model aur Scaler load karo
model = joblib.load('churn_model.pkl')
scaler = joblib.load('scaler.pkl')

st.title("Bank Customer Churn Predictor")

# Input fields
age = st.number_input("Age", 18, 100)
balance = st.number_input("Balance", 0, 500000)

if st.button("Predict"):
    # Input ko 2D array mein convert karo
    input_data = np.array([[age, balance]])
    
    # Scaling (Bahut zaroori step)
    input_data_scaled = scaler.transform(input_data)
    
    # Prediction
    prediction = model.predict(input_data_scaled)
    
    if prediction[0] == 1:
        st.write("Customer will Churn.")
    else:
        st.write("Customer will not Churn.")
