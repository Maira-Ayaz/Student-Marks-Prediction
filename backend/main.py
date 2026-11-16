
from fastapi import FastAPI
from pydantic import BaseModel, Field
from pathlib import Path
import joblib

# Create FastAPI application
app = FastAPI(title="Student Marks Prediction API")


# Get the main project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load the saved ML model
MODEL_PATH = BASE_DIR / "models" / "linear_regression_model.joblib"

model = joblib.load(MODEL_PATH)


# Pydantic model for input validation
class Student(BaseModel):
    study_hours: float = Field(ge=0, le=24)


# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Student Marks Prediction API is running!"
    }


# Health check endpoint
@app.get("/health")
def health():
    return {"status": "healthy"}


# Prediction endpoint
@app.post("/predict")
def predict_marks(student: Student):

    # Get study hours
    hours = student.study_hours

    # Predict marks using saved model
    prediction = model.predict([[hours]])

    # Return prediction
    return {
        "study_hours": hours,
        "predicted_marks": round(float(prediction[0]), 2)
    }
