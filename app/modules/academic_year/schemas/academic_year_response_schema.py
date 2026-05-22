from datetime import date, datetime
from uuid import UUID

from pydantic import BaseModel


class AcademicYearResponseSchema(BaseModel):
    id: UUID
    name: str
    start_date: date
    end_date: date
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True