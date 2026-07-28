import streamlit as st
import joblib
import pandas as pd

# Load Model
model = joblib.load("churn_model_compressed.pkl")

st.set_page_config(page_title="Bank Customer Churn Prediction", page_icon="🏦", layout="centered")

st.title("🏦 Bank Customer Churn Prediction")
st.write("Fill the customer details and click Predict.")

credit_score = st.number_input("Credit Score", 300, 900, 650)
age = st.number_input("Age", 18, 100, 35)
tenure = st.number_input("Tenure (Years)", 0, 10, 5)
balance = st.number_input("Balance", 0.0, 300000.0, 50000.0)
num_products = st.number_input("Number of Products", 1, 4, 2)
has_card = st.selectbox("Has Credit Card?", ["Yes", "No"])
active = st.selectbox("Is Active Member?", ["Yes", "No"])
salary = st.number_input("Estimated Salary", 0.0, 300000.0, 50000.0)
satisfaction = st.slider("Satisfaction Score", 1, 5, 3)
points = st.number_input("Points Earned", 0, 1000, 300)

geo = st.selectbox("Geography", ["France", "Germany", "Spain"])
gender = st.selectbox("Gender", ["Female", "Male"])
card = st.selectbox("Card Type", ["DIAMOND", "GOLD", "PLATINUM", "SILVER"])

# One-Hot Encoding
geo_germany = 1 if geo == "Germany" else 0
geo_spain = 1 if geo == "Spain" else 0

gender_male = 1 if gender == "Male" else 0

card_gold = 1 if card == "GOLD" else 0
card_platinum = 1 if card == "PLATINUM" else 0
card_silver = 1 if card == "SILVER" else 0

has_card = 1 if has_card == "Yes" else 0
active = 1 if active == "Yes" else 0

input_df = pd.DataFrame([{
    "CreditScore": credit_score,
    "Age": age,
    "Tenure": tenure,
    "Balance": balance,
    "NumOfProducts": num_products,
    "HasCrCard": has_card,
    "IsActiveMember": active,
    "EstimatedSalary": salary,
    "Satisfaction Score": satisfaction,
    "Point Earned": points,
    "Geography_Germany": geo_germany,
    "Geography_Spain": geo_spain,
    "Gender_Male": gender_male,
    "Card Type_GOLD": card_gold,
    "Card Type_PLATINUM": card_platinum,
    "Card Type_SILVER": card_silver
}])

if st.button("Predict Churn"):

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    if prediction == 1:
        st.error(f"⚠️ Customer is likely to Churn ({probability*100:.2f}%)")
    else:
        st.success(f"✅ Customer is likely to Stay ({(1-probability)*100:.2f}%)")
