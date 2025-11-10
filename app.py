import streamlit as st
import numpy as np
import joblib
import pandas as pd

scaler = joblib.load('scaler.pkl')
model = joblib.load('best_model.pkl')
le_gender = joblib.load('label_encoder_gender.pkl')
le_smoker = joblib.load('label_encoder_smoker.pkl')
le_diabetic = joblib.load('label_encoder_diabetic.pkl')

st.set_page_config(page_title="Health Insurance Cost Predictor", page_icon=":hospital:", layout="centered")
st.title("Health Insurance Payment Predictor App")
st.write("Enter the details below to predict the health insurance payment amount.")

with st.form("input_form"):
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age", min_value=0, max_value=120, value=30)
        bmi = st.number_input("BMI", min_value=0.0, max_value=100.0, value=25.0)
        children = st.number_input("Number of Children", min_value=0, max_value=20, value=0)
    with col2:
        bloodpressure = st.number_input("Blood Pressure", min_value=0, max_value=300, value=120)  # Changed variable name
        gender = st.selectbox("Gender", options=le_gender.classes_)
        diabetic = st.selectbox("Diabetic", options=le_diabetic.classes_)
        smoker = st.selectbox("Smoker", options=le_smoker.classes_)
    
    submitted = st.form_submit_button("Predict Payment")

if submitted:
    input_data = pd.DataFrame({
        'age': [age],
        'gender': [gender],
        'bmi': [bmi],
        'bloodpressure': [bloodpressure],  # Changed to match training data
        'diabetic': [diabetic],
        'children': [children],
        'smoker': [smoker],
    })
    
    # Transform categorical variables
    input_data['gender'] = le_gender.transform(input_data['gender'])
    input_data['diabetic'] = le_diabetic.transform(input_data['diabetic'])  
    input_data['smoker'] = le_smoker.transform(input_data['smoker'])

    # Scale numerical features - ensure these columns match what scaler was fitted on
    num_cols = ['age', 'bmi', 'bloodpressure', 'children']  # Updated column name
    input_data[num_cols] = scaler.transform(input_data[num_cols])

    # Ensure column order matches training data
    # You might need to reorder columns to match the training data
    expected_columns = ['age', 'gender', 'bmi', 'bloodpressure', 'diabetic', 'children', 'smoker']
    input_data = input_data[expected_columns]
    
    predict = model.predict(input_data)[0]

    st.success(f"**Estimated Insurance Payment Amount**: ${predict:.2f}")