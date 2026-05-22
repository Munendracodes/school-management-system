from sqlalchemy.orm import Session

from app.modules.users.models.user_model import UserModel
from app.modules.users.repositories.user_repository import (
    UserRepository,
)
from app.modules.users.schemas.auth_schema import (
    LoginRequest,
    LoginResponse,
    ResetPasswordRequest,
    UserInfo,
)
from app.modules.users.utils.jwt_handler import (
    create_access_token,
)

from app.core.auth.password import (
    PasswordService,
)

from app.modules.users.schemas.user_schema import (
    UserResponse
)

class AuthService:

    @staticmethod
    def login(
        db: Session,
        payload: LoginRequest
    ) -> LoginResponse:
        print("AuthService.login called with mobile_number:", payload.mobile_number, "and password:", payload.password)
        user = UserRepository.get_by_mobile_number(
            db,
            payload.mobile_number
        )

        userdata_response = UserResponse.from_orm(user) if user else None
        print("AuthService.login called with mobile_number:", payload.mobile_number, "found user:", userdata_response)

        if not user:
            raise ValueError(
                "Invalid mobile number or password"
            )

        print("payload password:", payload.password)
        print("user password hash:", user.password_hash)

        if not PasswordService.verify_password(
            payload.password,
            user.password_hash
        ):
            print("Password verification failed for mobile number:", payload.mobile_number)
            raise ValueError(
                "Invalid mobile number or password"
            )

        if not user.is_active:
            raise ValueError(
                "User account is inactive"
            )

        access_token = create_access_token(
            {
                "user_id": str(user.id),
                "role": user.role.name
            }
        )

        return LoginResponse(
            access_token=access_token,
            requires_password_reset=user.is_first_login,
            user=UserInfo(
                id=str(user.id),
                full_name=user.full_name,
                mobile_number=user.mobile_number,
                role=user.role.name
            )
        )
    
    @staticmethod
    def reset_password(
        db: Session,
        current_user: UserModel,
        payload: ResetPasswordRequest
    ):

        is_valid_password = PasswordService.verify_password(
            payload.old_password,
            current_user.password_hash
        )

        if not is_valid_password:
            raise ValueError(
                "Current password is incorrect"
            )

        hashed_password = PasswordService.hash_password(
            payload.new_password
        )

        current_user.password_hash = (
            hashed_password
        )

        current_user.is_first_login = False

        db.commit()
        db.refresh(current_user)

        return {
            "message": (
                "Password reset successfully"
            )
        }