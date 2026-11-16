
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Student(BaseModel):
    name: str
    age: int
    marks: int


# GET: Home endpoint
@app.get("/")
def home():
    return {"message": "Hello my first API"}


# POST: Create student
@app.post("/student")
def create_student(student: Student):
    try:
        return {
            "message": "Student added successfully",
            "student_data": student
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# GET: Get student by ID
@app.get("/students/{student_id}")
def get_student(student_id: int):
    return {"student_id": student_id}


# DELETE: Delete student by ID
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    return {"message": f"Student {student_id} deleted"}


class StudentUpdate(BaseModel):
    marks: int | None = None


@app.patch("/students/{student_id}")
def update_student(student_id: int, student: StudentUpdate):

    return {
        "message": "Student updated successfully",
        "student_id": student_id,
        "updated_data": student.model_dump(exclude_unset=True)
    }