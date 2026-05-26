from datetime import date, datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


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