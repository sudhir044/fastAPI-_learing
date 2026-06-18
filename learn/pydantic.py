from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    student_id: int
    name: str
    age: int
    grade: str
    marks: float

    @app.post("/students")
    def create_student(student: Student):
        return {
            "message": "Student created successfully",
            "student": student
        }
