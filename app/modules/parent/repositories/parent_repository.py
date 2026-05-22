from sqlalchemy import select
from sqlalchemy.orm import Session

from app.modules.parent.models.parent_model import Parent
from app.modules.parent.models.student_parent_mapping_model import (
    StudentParentMapping,
)


class ParentRepository:

    @staticmethod
    def create(
        db: Session,
        payload: dict,
    ):
        parent = Parent(**payload)

        db.add(parent)

        db.commit()
        db.refresh(parent)

        return parent

    @staticmethod
    def get_all(
        db: Session,
    ):
        query = select(Parent).where(
            Parent.is_deleted == False,
        )

        return db.scalars(query).all()

    @staticmethod
    def get_by_id(
        db: Session,
        parent_id: str,
    ):
        query = select(Parent).where(
            Parent.id == parent_id,
            Parent.is_deleted == False,
        )

        return db.scalar(query)

    @staticmethod
    def get_by_mobile_number(
        db: Session,
        mobile_number: str,
    ):
        query = select(Parent).where(
            Parent.mobile_number == mobile_number,
            Parent.is_deleted == False,
        )

        return db.scalar(query)

    @staticmethod
    def update(
        db: Session,
        parent: Parent,
        payload: dict,
    ):
        for key, value in payload.items():
            setattr(parent, key, value)

        db.commit()
        db.refresh(parent)

        return parent

    @staticmethod
    def soft_delete(
        db: Session,
        parent: Parent,
    ):
        parent.is_deleted = True

        db.commit()

    @staticmethod
    def create_student_parent_mapping(
        db: Session,
        payload: dict,
    ):
        mapping = StudentParentMapping(**payload)

        db.add(mapping)

        db.commit()
        db.refresh(mapping)

        return mapping