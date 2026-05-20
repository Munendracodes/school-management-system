from uuid import UUID

from sqlalchemy import or_
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
        user_id: UUID
    ) -> UserModel | None:

        return (
            db.query(UserModel)
            .filter(
                UserModel.id == user_id,
                UserModel.is_deleted == False
            )
            .first()
        )

    @staticmethod
    def get_by_mobile_number(
        db: Session,
        mobile_number: str
    ) -> UserModel | None:

        return (
            db.query(UserModel)
            .filter(
                UserModel.mobile_number == mobile_number,
                UserModel.is_deleted == False
            )
            .first()
        )

    @staticmethod
    def get_by_email(
        db: Session,
        email: str
    ) -> UserModel | None:

        return (
            db.query(UserModel)
            .filter(
                UserModel.email == email,
                UserModel.is_deleted == False
            )
            .first()
        )

    @staticmethod
    def get_users(
        db: Session,
        page: int,
        size: int,
        search: str | None = None,
        role_id: UUID | None = None,
        is_active: bool | None = None
    ):

        query = db.query(UserModel).filter(
            UserModel.is_deleted == False
        )

        if search:
            query = query.filter(
                or_(
                    UserModel.full_name.ilike(f"%{search}%"),
                    UserModel.mobile_number.ilike(f"%{search}%")
                )
            )

        if role_id:
            query = query.filter(
                UserModel.role_id == role_id
            )

        if is_active is not None:
            query = query.filter(
                UserModel.is_active == is_active
            )

        total = query.count()

        users = (
            query
            .offset((page - 1) * size)
            .limit(size)
            .all()
        )

        return users, total

    @staticmethod
    def update(
        db: Session,
        user: UserModel,
        update_data: dict
    ) -> UserModel:

        for key, value in update_data.items():
            setattr(user, key, value)

        db.commit()
        db.refresh(user)

        return user

    @staticmethod
    def soft_delete(
        db: Session,
        user: UserModel
    ):

        user.is_deleted = True

        db.commit()