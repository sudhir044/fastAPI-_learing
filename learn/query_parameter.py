from fastapi import FastAPI

app = FastAPI()

students = {
    "S001": {"name": "sudhir", "age": 20,"subject":"python", "grade": "A"},
    "S002": {"name": "Jane", "age": 22,"subject":"java", "grade": "B"},
    "S003": {"name": "Doe", "age": 21,"subject":"c++", "grade": "C"}
}

@app.get("/students")
def get_students(grade: str):
    student_list = [student for student in students.values() if student["grade"] == grade]
    return {"grade": grade, "students": student_list}