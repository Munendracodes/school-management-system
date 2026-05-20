from uuid import UUID

from sqlalchemy.orm import Session

from app.modules.users.repositories.role_repository import (
    RoleRepository,
)


class RoleService:

    @staticmethod
    def get_roles(
        db: Session
    ):

        roles = RoleRepository.get_all(
            db
        )

        return {
            "items": roles
        }

    @staticmethod
    def get_role_by_id(
        db: Session,
        role_id: UUID
    ):

        role = RoleRepository.get_by_id(
            db,
            role_id
        )

        if not role:
            raise ValueError(
                "Role not found"
            )

        return role