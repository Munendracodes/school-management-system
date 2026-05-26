from uuid import UUID
from typing import Optional, List
from datetime import date

from pydantic import (
    BaseModel,
    ConfigDict,
)


# --------------------------
# Nested Schemas
# --------------------------

class ClassroomShortSchema(BaseModel):

    id: UUID
    name: str

    model_config = ConfigDict(
        from_attributes=True
    )


class SectionShortSchema(BaseModel):

    id: UUID
    name: str

    model_config = ConfigDict(
        from_attributes=True
    )


class AcademicYearShortSchema(BaseModel):

    id: UUID
    name: str

    model_config = ConfigDict(
        from_attributes=True
    )


class ParentShortSchema(BaseModel):

    id: UUID
    full_name: str
    relationship_type: str

    model_config = ConfigDict(
        from_attributes=True
    )


# --------------------------
# Create / Update
# --------------------------

class StudentCreateSchema(BaseModel):

    admission_number: str
    full_name: str
    gender: str
    date_of_birth: date

    section_id: UUID


class StudentUpdateSchema(BaseModel):

    admission_number: Optional[str] = None
    full_name: Optional[str] = None
    gender: Optional[str] = None
    date_of_birth: Optional[date] = None

    section_id: Optional[UUID] = None


# --------------------------
# Response
# --------------------------

class StudentResponseSchema(BaseModel):

    id: UUID
    admission_number: str
    full_name: str
    gender: str
    date_of_birth: date

    classroom: ClassroomShortSchema
    section: SectionShortSchema
    academic_year: AcademicYearShortSchema

    parents: List[
        ParentShortSchema
    ] = []

    model_config = ConfigDict(
        from_attributes=True
    )