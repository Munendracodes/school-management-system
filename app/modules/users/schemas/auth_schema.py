from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    mobile_number: str = Field(
        ...,
        min_length=10,
        max_length=15,
        examples=["9876543210"]
    )

    password: str = Field(
        ...,
        min_length=4,
        examples=["1234"]
    )


class UserInfo(BaseModel):
    id: str
    full_name: str
    mobile_number: str
    role: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    requires_password_reset: bool
    user: UserInfo


class ResetPasswordRequest(BaseModel):
    old_password: str = Field(
        ...,
        min_length=4,
    )

    new_password: str = Field(
        ...,
        min_length=4
    )