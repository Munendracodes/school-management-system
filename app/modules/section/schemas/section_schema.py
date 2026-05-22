from uuid import UUID
from typing import Optional

from pydantic import BaseModel


class SectionCreateSchema(BaseModel):

    name: str
    classroom_id: UUID
    capacity: int = 40
    display_order: int = 1


class SectionUpdateSchema(BaseModel):

    name: Optional[str] = None
    capacity: Optional[int] = None
    display_order: Optional[int] = None
    is_active: Optional[bool] = None


class SectionResponseSchema(BaseModel):

    id: UUID
    name: str
    classroom_id: UUID
    capacity: int
    display_order: int
    is_active: bool

    class Config:
        from_attributes = True