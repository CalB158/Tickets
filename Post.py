from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    lastname: str

@app.post("/students")
def saveStudent(student: Student):
    return f"Estudiantes {student.name}: {student.lastname} guardado"
