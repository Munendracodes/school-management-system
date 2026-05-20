from math import ceil
from uuid import UUID

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
    UpdateUserRequest,
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
    ):

        existing_mobile = (
            UserRepository.get_by_mobile_number(
                db,
                payload.mobile_number
            )
        )

        if existing_mobile:
            raise ValueError(
                "Mobile number already exists"
            )

        if payload.email:

            existing_email = (
                UserRepository.get_by_email(
                    db,
                    payload.email
                )
            )

            if existing_email:
                raise ValueError(
                    "Email already exists"
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

        user = UserRepository.create(
            db,
            user_data
        )

        return {
            "message": "User created successfully",
            "temporary_pin": temporary_pin,
            "user": user
        }

    @staticmethod
    def get_users(
        db: Session,
        page: int,
        size: int,
        search: str | None = None,
        role_id: UUID | None = None,
        is_active: bool | None = None
    ):

        users, total = UserRepository.get_users(
            db=db,
            page=page,
            size=size,
            search=search,
            role_id=role_id,
            is_active=is_active
        )

        return {
            "items": users,
            "total": total,
            "page": page,
            "size": size,
            "pages": ceil(total / size)
        }

    @staticmethod
    def get_user_by_id(
        db: Session,
        user_id: UUID
    ):

        user = UserRepository.get_by_id(
            db,
            user_id
        )

        if not user:
            raise ValueError(
                "User not found"
            )

        return user

    @staticmethod
    def update_user(
        db: Session,
        user_id: UUID,
        payload: UpdateUserRequest
    ):

        user = UserRepository.get_by_id(
            db,
            user_id
        )

        if not user:
            raise ValueError(
                "User not found"
            )

        update_data = payload.model_dump(
            exclude_unset=True
        )

        updated_user = UserRepository.update(
            db,
            user,
            update_data
        )

        return updated_user

    @staticmethod
    def delete_user(
        db: Session,
        user_id: UUID
    ):

        user = UserRepository.get_by_id(
            db,
            user_id
        )

        if not user:
            raise ValueError(
                "User not found"
            )

        UserRepository.soft_delete(
            db,
            user
        )

        return {
            "message": "User deleted successfully"
        }