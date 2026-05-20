from uuid import UUID
from datetime import datetime

from pydantic import BaseModel


class RoleResponse(BaseModel):
    id: UUID
    name: str
    description: str | None
    created_at: datetime

    class Config:
        from_attributes = True


class RoleListResponse(BaseModel):
    items: list[RoleResponse]