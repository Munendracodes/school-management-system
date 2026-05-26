from uuid import UUID
from typing import Optional, List

from pydantic import BaseModel, ConfigDict


# --------------------------
# Nested Schemas
# --------------------------

class SectionShortSchema(BaseModel):
    id: UUID
    name: str

    model_config = ConfigDict(from_attributes=True)


class ClassroomShortSchema(BaseModel):
    id: UUID
    name: str

    model_config = ConfigDict(from_attributes=True)


class AcademicYearShortSchema(BaseModel):
    id: UUID
    name: str

    model_config = ConfigDict(from_attributes=True)


class ChildStudentSchema(BaseModel):
    id: UUID
    full_name: str

    section: SectionShortSchema
    classroom: ClassroomShortSchema
    academic_year: AcademicYearShortSchema

    relationship_type: str

    model_config = ConfigDict(
        from_attributes=True
    )


# --------------------------
# Parent Create / Update
# --------------------------

class ParentCreateSchema(BaseModel):
    full_name: str
    mobile_number: str
    email: Optional[str] = None


class ParentUpdateSchema(BaseModel):
    full_name: Optional[str] = None
    mobile_number: Optional[str] = None
    email: Optional[str] = None


# --------------------------
# Parent Response
# --------------------------

class ParentResponseSchema(BaseModel):

    id: UUID
    full_name: str
    mobile_number: str
    email: Optional[str]

    children: List[ChildStudentSchema] = []

    model_config = ConfigDict(
        from_attributes=True
    )


# --------------------------
# Mapping
# --------------------------

class StudentParentMappingCreateSchema(BaseModel):
    student_id: UUID
    parent_id: UUID


class StudentParentMappingResponseSchema(BaseModel):
    student_id: UUID
    parent_id: UUID

    model_config = ConfigDict(
        from_attributes=True
    )