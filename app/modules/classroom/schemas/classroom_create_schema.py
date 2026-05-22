from uuid import UUID

from pydantic import BaseModel


class ClassRoomCreateSchema(BaseModel):
    name: str
    display_order: int
    academic_year_id: UUID
    is_active: bool = True