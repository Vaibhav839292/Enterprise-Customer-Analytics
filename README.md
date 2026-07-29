# Enterprise Customer Churn Analytics & Prediction Platform

## Executive Summary
The Enterprise Customer Churn Analytics platform is an end-to-end machine learning application engineered to predict and analyze bank customer churn. By leveraging predictive modeling and behavioral analytics, this solution empowers financial institutions to proactively identify retention risks, optimize customer lifecycle management, and execute data-driven intervention strategies.

---

## Live Demonstration & Access
* **Production Deployment:** [Access Live Streamlit Application](https://enterprise-customer-analytics-vorrfvph4dpnnbutnuabok.streamlit.app)

---

## Technical Architecture & Core Competencies
The system integrates modern data science frameworks with a robust, production-grade cloud deployment architecture.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-Learn">
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy">
  <img src="https://img.shields.io/badge/Machine_Learning-00599C?style=for-the-badge&logo=databricks&logoColor=white" alt="Machine Learning">
  <img src="https://img.shields.io/badge/Joblib-4285F4?style=for-the-badge&logo=python&logoColor=white" alt="Joblib">
</p>

---

## Repository File Structure
```text
Enterprise-Customer-Analytics/
│
├── app.py                         # Core Streamlit web application interface
├── Churn_Prediction_Project.ipynb # Exploratory Data Analysis & Model Training Pipeline
├── Customer-Churn-Records.csv     # Historical enterprise dataset for analytics
├── churn_model_compressed.pkl     # Serialized classification model weights
├── scaler_compressed.pkl          # Standardized preprocessing feature parameters
└── requirements.txt               # Dependency configuration for deployment environments

