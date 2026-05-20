from typing import Optional

from pydantic import BaseModel, EmailStr, Field
from typing import Optional



class CreateUserRequest(BaseModel):
    full_name: str = Field(
        ...,
        min_length=2,
        max_length=100,
        examples=["John Doe"]
    )

    mobile_number: str = Field(
        ...,
        min_length=10,
        max_length=15,
        examples=["9876543210"]
    )

    email: Optional[EmailStr] = Field(
        default=None,
        examples=["john@example.com"]
    )

    role_id: str


class UpdateUserRequest(BaseModel):
    full_name: Optional[str] = Field(
        default=None,
        min_length=2,
        max_length=100
    )

    email: Optional[EmailStr] = None

    is_active: Optional[bool] = None


class UserResponse(BaseModel):
    id: str
    full_name: str
    mobile_number: str
    email: Optional[str]
    role: str
    is_active: bool
    is_first_login: bool