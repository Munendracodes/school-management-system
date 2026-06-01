from sqlalchemy import (
    select,
    func,
)
from sqlalchemy.orm import Session

from app.modules.student_parent_map.models.student_parent_map_model import (
    StudentParentMap,
)


class StudentParentMapRepository:

    @staticmethod
    def create(
        db: Session,
        payload: dict,
        commit: bool = True,
    ):
        mapping = StudentParentMap(
            **payload
        )

        db.add(
            mapping
        )

        if commit:
            db.commit()
            db.refresh(
                mapping
            )

        return mapping

    @staticmethod
    def exists(
        db: Session,
        student_id,
        parent_id,
    ):
        query = (
            select(StudentParentMap)
            .where(
                StudentParentMap.student_id == student_id,
                StudentParentMap.parent_id == parent_id,
                StudentParentMap.is_deleted.is_(False),
            )
        )

        return db.scalar(
            query
        )

    @staticmethod
    def get_by_student_and_relationship(
        db: Session,
        student_id,
        relationship_type: str,
    ):
        query = (
            select(StudentParentMap)
            .where(
                StudentParentMap.student_id == student_id,
                func.lower(
                    StudentParentMap.relationship_type
                )
                == relationship_type.lower(),
                StudentParentMap.is_deleted.is_(False),
            )
        )

        return db.scalar(
            query
        )