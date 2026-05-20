from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.modules.users.dependencies.current_user import (
    get_current_user,
)

from app.modules.users.models.user_model import (
    UserModel,
)

from app.modules.users.schemas.auth_schema import (
    LoginRequest,
    LoginResponse,
    ResetPasswordRequest,
)

from app.modules.users.services.auth_service import (
    AuthService,
)


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/login",
    response_model=LoginResponse
)
def login(
    payload: LoginRequest,
    db: Session = Depends(get_db)
):

    try:
        return AuthService.login(
            db,
            payload
        )

    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(error)
        )


@router.post("/reset-password")
def reset_password(
    payload: ResetPasswordRequest
):

    return {
        "message": (
            "Reset password API "
            "will be implemented next"
        )
    }


@router.get("/me")
def get_me(
    current_user: UserModel = Depends(
        get_current_user
    )
):

    return {
        "id": str(current_user.id),
        "full_name": current_user.full_name,
        "mobile_number": current_user.mobile_number,
        "email": current_user.email,
        "role": current_user.role.name,
        "is_active": current_user.is_active
    }