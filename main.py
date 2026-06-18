from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Student(BaseModel):
    student_id: int
    name: str
    age: int
    grade: str
    marks: float


@app.get("/")
def home():
    return {"message": "Hello, World!"}


@app.post("/students")
def create_student(student: Student):
    return student


students = {
    1: {"name": "John", "age": 20, "grade": "A", "marks": 85.5},
    2: {"name": "Jane", "age": 22, "grade": "B", "marks": 78.0},
    3: {"name": "Doe", "age": 21, "grade": "C", "marks": 65.0},
}


@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id in students:
        return students[student_id]
    return {"error": "Student not found"}


@app.get("/students")
def get_students():
    return students

@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    if student_id in students:
        students[student_id] = student.dict()
        return {"message": "Student updated"}
    return {"error": "Student not found"}

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id in students:
        del students[student_id]
        return {"message": "Student deleted"}
    return {"error": "Student not found"}