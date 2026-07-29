# 🏦 Enterprise Customer Churn Analytics & Prediction App

An end-to-end Machine Learning web application built to predict bank customer churn. This project helps financial institutions identify customers who are likely to leave, enabling proactive retention strategies and data-driven business decisions.

<p align="center">
  <a href="https://enterprise-customer-analytics-vorrfvph4dpnnbutnuabok.streamlit.app" target="_blank">
    <img src="https://img.shields.io/badge/🚀_View_Live_App-Streamlit-ff4b4b?style=for-the-badge&logo=streamlit&logoColor=white" alt="Live App">
  </a>
</p>

---

## 🛠️ Tech Stack & Skills Used

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-Learn">
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy">
  <img src="https://img.shields.io/badge/Machine_Learning-00599C?style=for-the-badge&logo=databricks&logoColor=white" alt="Machine Learning">
  <img src="https://img.shields.io/badge/Joblib-4285F4?style=for-the-badge&logo=python&logoColor=white" alt="Joblib">
</p>

---

## 📂 Project Directory Structure

```text
Enterprise-Customer-Analytics/
│
├── app.py                      # Main Streamlit web application script
├── Churn_Prediction_Project.ipynb # Jupyter Notebook containing EDA & Model Training
├── Customer-Churn-Records.csv  # Raw dataset used for analysis and training
├── churn_model_compressed.pkl  # Trained machine learning model weights
├── scaler_compressed.pkl       # Feature scaling parameters for preprocessing
└── requirements.txt            # Required Python packages for cloud deployment
🚀 Key Features
Real-Time Predictions: Instantly analyze customer behavior parameters to predict churn risk.

Interactive Web Interface: Developed with Streamlit to offer a clean, responsive, and user-friendly control panel.

Automated Data Preprocessing: Scales user inputs in real-time using pre-trained StandardScaler objects.

Production-Ready Deployment: Hosted live on Streamlit Cloud for seamless accessibility from anywhere.

⚙️ Local Setup and Installation
If you want to clone and run this application locally on your machine, follow these steps:

Clone the repository:

Bash
git clone [https://github.com/Vaibhav839292/Enterprise-Customer-Analytics.git](https://github.com/Vaibhav839292/Enterprise-Customer-Analytics.git)
cd Enterprise-Customer-Analytics
Install the dependencies:

Bash
pip install -r requirements.txt
Run the application:

Bash
streamlit run app.py
📈 Machine Learning Workflow
Exploratory Data Analysis (EDA): Analyzed customer trends, financial records, and behavior metrics using Jupyter Notebook.

Data Preprocessing & Scaling: Handled numerical normalization to ensure stable model performance.

Model Training & Evaluation: Trained classification models via scikit-learn to maximize prediction accuracy.

Model Serialization: Compressed and saved the trained components securely using joblib.

Deployment: Integrated serialized assets into a web framework for real-time user interaction.

👨‍💻 Author
Vaibhav

GitHub: @Vaibhav839292


