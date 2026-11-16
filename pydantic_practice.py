
from pydantic import BaseModel, ValidationError

# Creating Pydantic model
class Student(BaseModel):
    name: str
    age: int
    marks: int


# Taking input from user
name = input("Enter student name: ")
age = input("Enter student age: ")
marks = input("Enter student marks: ")

# Validating user input
try:
    student = Student(
        name=name,
        age=age,
        marks=marks
    )

    print("\nStudent created successfully!")
    print(student)

except ValidationError as e:
    print("\nInvalid student data!")
    print(e)
