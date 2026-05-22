from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class ClassRoomUpdateSchema(BaseModel):
    name: Optional[str] = None
    display_order: Optional[int] = None
    academic_year_id: Optional[UUID] = None
    is_active: Optional[bool] = None