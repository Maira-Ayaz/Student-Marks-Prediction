
import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load("models/linear_regression_model.joblib")

# Application title
st.title("Student Marks Predictor")

# Description
st.write("Predict your marks based on your study hours.")

# Take input from user
hours = st.number_input(
    "Enter your study hours:",
    min_value=1.0,
    max_value=10.0,
    value=5.0,
    step=0.5
)

# Predict button
if st.button("Predict Marks"):

    # Convert input into DataFrame
    user_input = pd.DataFrame({
        "Study_Hours": [hours]
    })

    # Make prediction
    prediction = model.predict(user_input)

    # Display result
    st.success(f"Predicted Marks: {prediction[0]:.2f}")
