from datetime import date
from uuid import UUID
from typing import Optional

from pydantic import BaseModel


class TeacherCreateSchema(BaseModel):

    employee_id: str
    full_name: str
    gender: str
    mobile_number: str
    email: Optional[str] = None
    qualification: Optional[str] = None
    experience_years: int = 0
    joining_date: date
    is_class_teacher: bool = False


class TeacherUpdateSchema(BaseModel):

    full_name: Optional[str] = None
    gender: Optional[str] = None
    mobile_number: Optional[str] = None
    email: Optional[str] = None
    qualification: Optional[str] = None
    experience_years: Optional[int] = None
    joining_date: Optional[date] = None
    is_class_teacher: Optional[bool] = None
    is_active: Optional[bool] = None


class TeacherResponseSchema(BaseModel):

    id: UUID
    employee_id: str
    full_name: str
    gender: str
    mobile_number: str
    email: Optional[str]
    qualification: Optional[str]
    experience_years: int
    joining_date: date
    is_class_teacher: bool
    is_active: bool

    class Config:
        from_attributes = True


class TeacherSectionMappingCreateSchema(BaseModel):

    teacher_id: UUID
    section_id: UUID
    subject_name: str
    is_class_teacher: bool = False


class TeacherSectionMappingResponseSchema(BaseModel):

    id: UUID
    teacher_id: UUID
    section_id: UUID
    subject_name: str
    is_class_teacher: bool

    class Config:
        from_attributes = True