from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):
    id: int
    name: str
    department: str
    semester: int
    cgpa: float

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    department: Optional[str] = None
    semester: Optional[int] = None
    cgpa: Optional[float] = None