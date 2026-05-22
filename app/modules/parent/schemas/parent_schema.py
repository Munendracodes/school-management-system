from uuid import UUID
from typing import Optional

from pydantic import BaseModel


class ParentCreateSchema(BaseModel):

    father_name: Optional[str] = None
    mother_name: Optional[str] = None
    guardian_name: str
    mobile_number: str
    alternate_mobile_number: Optional[str] = None
    email: Optional[str] = None
    occupation: Optional[str] = None
    address: Optional[str] = None


class ParentUpdateSchema(BaseModel):

    father_name: Optional[str] = None
    mother_name: Optional[str] = None
    guardian_name: Optional[str] = None
    mobile_number: Optional[str] = None
    alternate_mobile_number: Optional[str] = None
    email: Optional[str] = None
    occupation: Optional[str] = None
    address: Optional[str] = None
    is_active: Optional[bool] = None


class ParentResponseSchema(BaseModel):

    id: UUID
    father_name: Optional[str]
    mother_name: Optional[str]
    guardian_name: str
    mobile_number: str
    alternate_mobile_number: Optional[str]
    email: Optional[str]
    occupation: Optional[str]
    address: Optional[str]
    is_active: bool

    class Config:
        from_attributes = True


class StudentParentMappingCreateSchema(BaseModel):

    student_id: UUID
    parent_id: UUID
    relationship_type: str


class StudentParentMappingResponseSchema(BaseModel):

    id: UUID
    student_id: UUID
    parent_id: UUID
    relationship_type: str

    class Config:
        from_attributes = True