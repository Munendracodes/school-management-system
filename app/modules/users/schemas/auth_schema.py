from pydantic import BaseModel, Field
from app.modules.users.utils.pin_generator import MPIN_REGEX


class LoginRequest(BaseModel):
    mobile_number: str = Field(
        ...,
        min_length=10,
        max_length=15,
        examples=["9876543210"]
    )

    password: str = Field(
        ...,
        pattern=MPIN_REGEX,
        min_length=4,
        max_length=4,
        examples=["1234"],
        description="4 digit MPIN code"
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
        pattern=MPIN_REGEX,
        min_length=4,
        max_length=4,
        examples=["1234"],
        description="4 digit MPIN code"
    )

    new_password: str = Field(
        ...,
        pattern=MPIN_REGEX,
        min_length=4,
        max_length=4,
        examples=["1234"],
        description="4 digit MPIN code"
    )