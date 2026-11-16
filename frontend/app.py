
import streamlit as st
import requests
import os

# Backend URL
BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "http://127.0.0.1:8000"
)

# Page configuration
st.set_page_config(
    page_title="Student Marks Prediction",
    page_icon="📚",
    layout="centered"
)

# Application title
st.title("📚 Student Marks Prediction")

st.write(
    "Predict your marks based on the number of hours you study."
)

st.divider()

# User input
with st.form("prediction_form"):

    hours = st.number_input(
        "Enter your study hours:",
        min_value=0.0,
        max_value=24.0,
        value=1.0,
        step=0.5
    )

    submitted = st.form_submit_button("Predict Marks")

# Make prediction
if submitted:

    data = {
        "study_hours": hours
    }

    try:
        response = requests.post(
            f"{BACKEND_URL}/predict",
            json=data,
            timeout=15
        )

        if response.status_code == 200:

            result = response.json()

            st.success("Prediction successful!")

            st.metric(
                label="Predicted Marks",
                value=result["predicted_marks"]
            )

            st.write(
                f"Study Hours: {result['study_hours']}"
            )

        else:
            st.error(
                f"Backend Error: {response.text}"
            )

    except requests.exceptions.ConnectionError:
        st.error(
            "Cannot connect to the backend. "
            "Please check whether FastAPI is running."
        )

    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {e}")
