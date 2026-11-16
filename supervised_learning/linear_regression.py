
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import joblib

# Load the dataset
df = pd.read_csv(r"C:\Users\User\Desktop\Machine_Learning\dataset\student_data.csv")
# Display first 5 records
print(df.head())

# Separate input (X) and output (y)

X = df[["Study_Hours"]]
y = df["Marks"]

# Display input and output
print("Input (X):")
print(X.head())

print("\nOutput (y):")
print(y.head())

# Split dataset into training and testing data

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Display shapes
print("X_train:", X_train.shape)
print("X_test:", X_test.shape)
print("y_train:", y_train.shape)
print("y_test:", y_test.shape)

# Select the Linear Regression model

model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

print("Model trained successfully!")
# Save the trained model
joblib.dump(model, "models/linear_regression_model.joblib")

print("Model saved successfully!")

# Make predictions using testing data
y_pred = model.predict(X_test)

# Display actual and predicted marks
print("Predicted Marks:")
print(y_pred)

print("\nActual Marks:")
print(y_test.values)

# Calculate model performance
accuracy = r2_score(y_test, y_pred)

print("Model R2 Score:", accuracy)
print("Model Accuracy:", accuracy * 100, "%")

# Take input from user
hours = float(input("Enter your study hours: "))

# Predict marks
user_input = pd.DataFrame({"Study_Hours": [hours]})

prediction = model.predict(user_input)

print("Predicted Marks:", prediction[0])
