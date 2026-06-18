from fastapi import FastAPI

app = FastAPI()

students = {
    "S001": {"name": "sudhir", "age": 20,"subject":"python"},
    "S002": {"name": "Jane", "age": 22,"subject":"java"},
    "S003": {"name": "Doe", "age": 21,"subject":"c++"}
}

@app.get("/students/{student_id}")
def get_student(student_id:str):


    if student_id in students:
        return students[student_id]
        return {"error": "Student not found"}




@app.get("/students/{student_id}/subject/{subject}")
def get_student_subject(student_id:str, subject:str):
    if student_id in students:
        return {
            "student_id": student_id,
            "subject": subject
        }
    return {"error": "Student or subject not found"}
