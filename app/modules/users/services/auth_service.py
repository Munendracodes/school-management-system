from sqlalchemy.orm import Session

from app.modules.users.repositories.user_repository import (
    UserRepository,
)
from app.modules.users.schemas.auth_schema import (
    LoginRequest,
    LoginResponse,
    UserInfo,
)
from app.modules.users.utils.jwt_handler import (
    create_access_token,
)
from app.modules.users.utils.password_handler import (
    verify_password,
)


class AuthService:

    @staticmethod
    def login(
        db: Session,
        payload: LoginRequest
    ) -> LoginResponse:

        user = UserRepository.get_by_mobile_number(
            db,
            payload.mobile_number
        )

        if not user:
            raise ValueError(
                "Invalid mobile number or password"
            )

        if not verify_password(
            payload.password,
            user.password_hash
        ):
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