from sqlalchemy import select
from sqlalchemy.orm import Session

from app.modules.users.models.user_model import UserModel


class UserRepository:

    @staticmethod
    def create(
        db: Session,
        user_data: dict
    ) -> UserModel:

        user = UserModel(**user_data)

        db.add(user)
        db.commit()
        db.refresh(user)

        return user

    @staticmethod
    def get_by_id(
        db: Session,
        user_id: str
    ) -> UserModel | None:

        query = select(UserModel).where(
            UserModel.id == user_id
        )

        result = db.execute(query)

        return result.scalar_one_or_none()

    @staticmethod
    def get_by_mobile_number(
        db: Session,
        mobile_number: str
    ) -> UserModel | None:

        query = select(UserModel).where(
            UserModel.mobile_number == mobile_number
        )

        result = db.execute(query)

        return result.scalar_one_or_none()

    @staticmethod
    def get_all(
        db: Session
    ) -> list[UserModel]:

        query = select(UserModel).order_by(
            UserModel.created_at.desc()
        )

        result = db.execute(query)

        return list(result.scalars().all())

    @staticmethod
    def update(
        db: Session,
        user: UserModel
    ) -> UserModel:

        db.add(user)
        db.commit()
        db.refresh(user)

        return user