from datetime import date, datetime
from uuid import UUID
from typing import Optional

from pydantic import BaseModel, ConfigDict


class AttendanceCreateSchema(BaseModel):

    student_id: UUID
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
    teacher_id: UUID

    attendance_date: date
    status: str
    remarks: Optional[str]

    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )