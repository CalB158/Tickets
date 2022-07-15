from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    lastname: str
    skills: list

@app.post("/students")
def saveStudent(student: Student):
    return f"Habilidades de {student.name}: {student.skills}"
