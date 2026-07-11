import streamlit as st
import pickle
import numpy as np

# Load model and scaler
# Python apne aap file ko dhund lega agar wo isi folder mein hai
model = pickle.load(open('churn_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

st.title("Bank Customer Churn Predictor")

# Inputs
age = st.number_input("Age", 18, 100)
balance = st.number_input("Balance", 0, 500000)

if st.button("Predict"):
    input_data = np.array([[age, balance]]) 
    scaled_data = scaler.transform(input_data)
    prediction = model.predict(scaled_data)
    
    if prediction[0] == 1:
        st.error("Customer is likely to CHURN!")
    else:
        st.success("Customer is LOYAL.")