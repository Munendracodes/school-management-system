from sqlalchemy.orm import Session

from app.modules.users.models.user_model import UserModel
from app.modules.users.repositories.role_repository import (
    RoleRepository,
)
from app.modules.users.repositories.user_repository import (
    UserRepository,
)
from app.modules.users.schemas.user_schema import (
    CreateUserRequest,
)
from app.modules.users.utils.password_handler import (
    hash_password,
)
from app.modules.users.utils.pin_generator import (
    generate_temporary_pin,
)


class UserService:

    @staticmethod
    def create_user(
        db: Session,
        payload: CreateUserRequest,
        created_by: str | None = None
    ) -> dict:

        existing_user = (
            UserRepository.get_by_mobile_number(
                db,
                payload.mobile_number
            )
        )

        if existing_user:
            raise ValueError(
                "Mobile number already exists"
            )

        role = RoleRepository.get_by_id(
            db,
            payload.role_id
        )

        if not role:
            raise ValueError(
                "Invalid role selected"
            )

        temporary_pin = generate_temporary_pin()

        hashed_password = hash_password(
            temporary_pin
        )

        user_data = {
            "full_name": payload.full_name,
            "mobile_number": payload.mobile_number,
            "email": payload.email,
            "password_hash": hashed_password,
            "role_id": role.id,
            "created_by": created_by,
            "is_active": True,
            "is_first_login": True
        }

        user: UserModel = UserRepository.create(
            db,
            user_data
        )

        return {
            "message": "User created successfully",
            "temporary_pin": temporary_pin,
            "user": {
                "id": str(user.id),
                "full_name": user.full_name,
                "mobile_number": user.mobile_number,
                "role": role.name
            }
        }

    @staticmethod
    def get_all_users(
        db: Session
    ) -> list[UserModel]:

        return UserRepository.get_all(db)