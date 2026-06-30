from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="University Registration API",
    description="API ساده برای مدیریت ثبت‌نام دانشجویان",
    version="1.0.0"
)

students_db = []

class Student(BaseModel):
    id: str
    name: str
    major: str

@app.get("/api/students", response_model=List[Student], tags=["Students"])
def get_all_students():
    return students_db

@app.post("/api/students", response_model=Student, status_code=201, tags=["Students"])
def add_student(student: Student):
    for s in students_db:
        if s.id == student.id:
            raise HTTPException(status_code=400, detail="دانشجویی با این شماره قبلاً ثبت شده است")
    
    students_db.append(student)
    return student

@app.get("/api/students/{student_id}", response_model=Student, tags=["Students"])
def get_student_by_id(student_id: str):
    for s in students_db:
        if s.id == student_id:
            return s
    
    raise HTTPException(status_code=404, detail="دانشجو یافت نشد")
