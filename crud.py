# crud.py
from database import students_db
from fastapi import HTTPException

def get_all_students():
    return students_db

def create_new_student(student_data: dict):
    for s in students_db:
        if s["id"] == student_data["id"]:
            raise HTTPException(status_code=400, detail="Student ID already exists")
    students_db.append(student_data)
    return student_data

def update_student_record(student_id: int, updated_data: dict):
    for s in students_db:
        if s["id"] == student_id:
            if updated_data.get("name") is not None: s["name"] = updated_data["name"]
            if updated_data.get("department") is not None: s["department"] = updated_data["department"]
            if updated_data.get("semester") is not None: s["semester"] = updated_data["semester"]
            if updated_data.get("cgpa") is not None: s["cgpa"] = updated_data["cgpa"]
            return s
    raise HTTPException(status_code=404, detail="Student not found")

def delete_student_record(student_id: int):
    for index, s in enumerate(students_db):
        if s["id"] == student_id:
            del students_db[index]
            return {"message": "Student deleted successfully"}
    raise HTTPException(status_code=404, detail="Student not found")