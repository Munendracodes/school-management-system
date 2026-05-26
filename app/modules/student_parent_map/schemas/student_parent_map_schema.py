from uuid import UUID

from pydantic import (
    BaseModel,
    ConfigDict,
)


class StudentParentMapCreateSchema(BaseModel):

    student_id: UUID
    parent_id: UUID
    relationship_type: str


class StudentParentMapResponseSchema(BaseModel):

    id: UUID

    student_id: UUID

    parent_id: UUID

    relationship_type: str

    model_config = ConfigDict(
        from_attributes=True
    )