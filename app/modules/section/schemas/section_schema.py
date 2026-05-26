from uuid import UUID
from typing import Optional
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class SectionCreateSchema(BaseModel):

    name: str
    classroom_id: UUID


class SectionUpdateSchema(BaseModel):

    name: Optional[str] = None
    classroom_id: Optional[UUID] = None


class SectionResponseSchema(BaseModel):

    id: UUID
    name: str
    classroom_id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )