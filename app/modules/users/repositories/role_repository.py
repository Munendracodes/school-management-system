from sqlalchemy import UUID, select
from sqlalchemy.orm import Session

from app.modules.users.models.role_model import RoleModel


class RoleRepository:

    @staticmethod
    def get_by_id(
        db: Session,
        role_id: UUID
    ) -> RoleModel | None:

        query = select(RoleModel).where(
            RoleModel.id == role_id
        )

        result = db.execute(query)

        return result.scalar_one_or_none()

    @staticmethod
    def get_by_name(
        db: Session,
        role_name: str
    ) -> RoleModel | None:

        query = select(RoleModel).where(
            RoleModel.name == role_name
        )

        result = db.execute(query)

        return result.scalar_one_or_none()

    @staticmethod
    def get_all(
        db: Session
    ) -> list[RoleModel]:

        query = select(RoleModel).order_by(
            RoleModel.name.asc()
        )

        result = db.execute(query)

        return list(result.scalars().all())