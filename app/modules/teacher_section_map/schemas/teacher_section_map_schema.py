from uuid import UUID

from pydantic import (
    BaseModel,
    ConfigDict,
)


class TeacherSectionMapCreateSchema(
    BaseModel
):

    teacher_id: UUID
    section_id: UUID
    subject_name: str


class TeacherSectionMapResponseSchema(
    BaseModel
):

    id: UUID

    teacher_id: UUID

    section_id: UUID

    subject_name: str

    model_config = ConfigDict(
        from_attributes=True
    )