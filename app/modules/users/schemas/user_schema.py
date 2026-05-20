from uuid import UUID
from datetime import datetime

from pydantic import BaseModel, EmailStr


class CreateUserRequest(BaseModel):
    full_name: str
    mobile_number: str
    email: EmailStr | None = None
    role_id: UUID


class UpdateUserRequest(BaseModel):
    full_name: str | None = None
    mobile_number: str | None = None
    email: EmailStr | None = None
    is_active: bool | None = None


class UserResponse(BaseModel):
    id: UUID
    full_name: str
    mobile_number: str
    email: str | None
    is_active: bool
    is_first_login: bool
    created_at: datetime

    class Config:
        from_attributes = True


class UserListResponse(BaseModel):
    items: list[UserResponse]
    total: int
    page: int
    size: int
    pages: int