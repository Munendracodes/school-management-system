from datetime import date
from uuid import UUID
from typing import Optional

from pydantic import BaseModel


class AttendanceCreateSchema(BaseModel):

    student_id: UUID
    section_id: UUID
    teacher_id: UUID
    attendance_date: date
    status: str
    remarks: Optional[str] = None


class AttendanceUpdateSchema(BaseModel):

    status: Optional[str] = None
    remarks: Optional[str] = None


class AttendanceResponseSchema(BaseModel):

    id: UUID
    student_id: UUID
    section_id: UUID
    teacher_id: UUID
    attendance_date: date
    status: str
    remarks: Optional[str]

    class Config:
        from_attributes = True