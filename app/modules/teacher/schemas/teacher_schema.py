from uuid import UUID
from typing import Optional, List

from pydantic import BaseModel, ConfigDict


# --------------------------
# Nested Section Schema
# --------------------------

class SectionShortSchema(BaseModel):
    id: UUID
    name: str

    model_config = ConfigDict(
        from_attributes=True
    )


# --------------------------
# Create / Update
# --------------------------

class TeacherCreateSchema(BaseModel):

    full_name: str
    mobile_number: str
    email: Optional[str] = None


class TeacherUpdateSchema(BaseModel):

    full_name: Optional[str] = None
    mobile_number: Optional[str] = None
    email: Optional[str] = None


# --------------------------
# Response
# --------------------------

class TeacherResponseSchema(BaseModel):

    id: UUID
    full_name: str
    mobile_number: str
    email: Optional[str]

    sections: List[SectionShortSchema] = []

    model_config = ConfigDict(
        from_attributes=True
    )


# --------------------------
# Teacher Section Mapping
# --------------------------

class TeacherSectionMappingCreateSchema(BaseModel):

    teacher_id: UUID
    section_id: UUID


class TeacherSectionMappingResponseSchema(BaseModel):

    teacher_id: UUID
    section_id: UUID

    model_config = ConfigDict(
        from_attributes=True
    )