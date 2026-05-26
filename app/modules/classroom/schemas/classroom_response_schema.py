from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ClassRoomResponseSchema(BaseModel):

    id: UUID
    academic_year_id: UUID
    name: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )