from datetime import date
from uuid import UUID
from typing import Optional

from pydantic import BaseModel


class StudentCreateSchema(BaseModel):

    admission_number: str
    full_name: str
    gender: str
    date_of_birth: date
    mobile_number: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    guardian_name: str
    guardian_mobile_number: str
    academic_year_id: UUID
    classroom_id: UUID
    section_id: UUID
    roll_number: str
    admission_date: date


class StudentUpdateSchema(BaseModel):

    full_name: Optional[str] = None
    gender: Optional[str] = None
    mobile_number: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    guardian_name: Optional[str] = None
    guardian_mobile_number: Optional[str] = None
    classroom_id: Optional[UUID] = None
    section_id: Optional[UUID] = None
    roll_number: Optional[str] = None
    is_active: Optional[bool] = None


class StudentResponseSchema(BaseModel):

    id: UUID
    admission_number: str
    full_name: str
    gender: str
    date_of_birth: date
    mobile_number: Optional[str]
    email: Optional[str]
    address: Optional[str]
    guardian_name: str
    guardian_mobile_number: str
    academic_year_id: UUID
    classroom_id: UUID
    section_id: UUID
    roll_number: str
    admission_date: date
    is_active: bool

    class Config:
        from_attributes = True