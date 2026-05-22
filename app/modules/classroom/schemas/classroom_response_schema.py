from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class ClassRoomResponseSchema(BaseModel):
    id: UUID
    name: str
    display_order: int
    academic_year_id: UUID
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True