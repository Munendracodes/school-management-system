from uuid import UUID
from pydantic import BaseModel


class ClassRoomCreateSchema(BaseModel):
    name: str
    academic_year_id: UUID