# main.py
from fastapi import FastAPI
from models import Student, StudentUpdate
from crud import get_all_students, create_new_student, update_student_record, delete_student_record
from chatbot import ask_chatbot

app = FastAPI(
    title="Student Database Application System",
    description="Backend API with Gemini and LangGraph chatbot integration",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Student Database API. Visit /docs for Swagger UI."}

@app.get("/students", response_model=list[Student])
def get_students():
    return get_all_students()

@app.post("/students", response_model=Student)
def create_student(student: Student):
    return create_new_student(student.dict())

@app.put("/students/{student_id}", response_model=Student)
def update_student(student_id: int, updated_data: StudentUpdate):
    return update_student_record(student_id, updated_data.dict())

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    return delete_student_record(student_id)

@app.post("/chat")
def chat_with_bot(query: str):
    response = ask_chatbot(query)
    return {"query": query, "response": response}