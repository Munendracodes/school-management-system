from fastapi import (
    HTTPException,
    status,
)

from sqlalchemy.orm import Session

from app.modules.parent.repositories.parent_repository import (
    ParentRepository,
)

from app.modules.student.repositories.student_repository import (
    StudentRepository,
)


class ParentService:

    @staticmethod
    def create_parent(
        db: Session,
        payload,
    ):
        existing_parent = ParentRepository.get_by_mobile_number(
            db,
            payload.mobile_number,
        )

        if existing_parent:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Mobile number already exists",
            )

        return ParentRepository.create(
            db,
            payload.model_dump(),
        )

    @staticmethod
    def get_parents(
        db: Session,
    ):
        return ParentRepository.get_all(db)

    @staticmethod
    def get_parent_by_id(
        db: Session,
        parent_id,
    ):
        parent = ParentRepository.get_by_id(
            db,
            parent_id,
        )

        if not parent:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Parent not found",
            )

        return parent

    @staticmethod
    def update_parent(
        db: Session,
        parent_id,
        payload,
    ):
        parent = ParentRepository.get_by_id(
            db,
            parent_id,
        )

        if not parent:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Parent not found",
            )

        return ParentRepository.update(
            db,
            parent,
            payload.model_dump(exclude_unset=True),
        )

    @staticmethod
    def delete_parent(
        db: Session,
        parent_id,
    ):
        parent = ParentRepository.get_by_id(
            db,
            parent_id,
        )

        if not parent:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Parent not found",
            )

        ParentRepository.soft_delete(
            db,
            parent,
        )

        return {
            "message": "Parent deleted successfully",
        }

    @staticmethod
    def map_student_parent(
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

        return ParentRepository.create_student_parent_mapping(
            db,
            payload.model_dump(),
        )