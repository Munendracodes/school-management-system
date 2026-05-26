from fastapi import (
    HTTPException,
    status,
)

from sqlalchemy.orm import Session

from app.modules.student.repositories.student_repository import (
    StudentRepository,
)

from app.modules.parent.repositories.parent_repository import (
    ParentRepository,
)

from app.modules.student_parent_map.repositories.student_parent_map_repository import (
    StudentParentMapRepository,
)


class StudentParentMapService:

    @staticmethod
    def create_mapping(
        db: Session,
        payload,
    ):

        student = StudentRepository.get_by_id(
            db,
            payload.student_id,
        )

        if not student:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Student not found",
            )

        parent = ParentRepository.get_by_id(
            db,
            payload.parent_id,
        )

        if not parent:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Parent not found",
            )

        exists = StudentParentMapRepository.exists(
            db,
            payload.student_id,
            payload.parent_id,
        )

        if exists:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Mapping already exists",
            )

        return StudentParentMapRepository.create(
            db,
            payload.model_dump(),
        )