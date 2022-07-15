from fastapi import FastAPI

app = FastAPI()

@app.post("/students")
def saveStudent(name: str, lastname: str):
    return f"Estudiante {name} {lastname} guardado!"