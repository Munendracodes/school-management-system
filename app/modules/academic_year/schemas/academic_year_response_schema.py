from datetime import date, datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict
from app.modules.classroom.schemas.classroom_response_schema import ClassWithSectionsResponseSchema


class AcademicYearResponseSchema(BaseModel):

    id: UUID
    name: str
    start_date: date
    end_date: date
    is_active: bool

    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )

class AcademicYearWithClassesResponseSchema(
    AcademicYearResponseSchema
):
    classrooms: list[ClassWithSectionsResponseSchema]

    model_config = ConfigDict(
        from_attributes=True
    )