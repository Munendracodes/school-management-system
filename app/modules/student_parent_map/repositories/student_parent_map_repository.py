from sqlalchemy.orm import Session

from app.modules.student_parent_map.models.student_parent_map_model import (
    StudentParentMap,
)


class StudentParentMapRepository:

    @staticmethod
    def create(
        db: Session,
        payload: dict,
    ):

        mapping = StudentParentMap(
            **payload
        )

        db.add(
            mapping
        )

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

        return (
            db.query(
                StudentParentMap
            )
            .filter(
                StudentParentMap.student_id == student_id,
                StudentParentMap.parent_id == parent_id,
                StudentParentMap.is_deleted == False,
            )
            .first()
        )