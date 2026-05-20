from typing import Optional

from pydantic import BaseModel


class CreateRoleRequest(BaseModel):
    name: str
    description: Optional[str] = None


class RoleResponse(BaseModel):
    id: str
    name: str
    description: Optional[str] = None