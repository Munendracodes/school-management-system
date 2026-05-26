from fastapi import (
    HTTPException,
    status,
)

from sqlalchemy.orm import Session

from app.modules.teacher.repositories.teacher_repository import (
    TeacherRepository,
)

from app.modules.section.repositories.section_repository import (
    SectionRepository,
)


class TeacherService:

    @staticmethod
    def create_teacher(
        db: Session,
        payload,
    ):

        existing_mobile = (
            TeacherRepository.get_by_mobile_number(
                db,
                payload.mobile_number,
            )
        )

        if existing_mobile:

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Mobile number already exists",
            )

        return TeacherRepository.create(
            db,
            payload.model_dump(),
        )

    @staticmethod
    def get_teachers(
        db: Session,
    ):

        return TeacherRepository.get_all(
            db
        )

    @staticmethod
    def get_teacher_by_id(
        db: Session,
        teacher_id,
    ):

        teacher = (
            TeacherRepository.get_by_id(
                db,
                teacher_id,
            )
        )

        if not teacher:

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Teacher not found",
            )

        return teacher

    @staticmethod
    def update_teacher(
        db: Session,
        teacher_id,
        payload,
    ):

        teacher = (
            TeacherRepository.get_by_id(
                db,
                teacher_id,
            )
        )

        if not teacher:

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Teacher not found",
            )

        return TeacherRepository.update(
            db,
            teacher,
            payload.model_dump(
                exclude_unset=True
            ),
        )

    @staticmethod
    def delete_teacher(
        db: Session,
        teacher_id,
    ):

        teacher = (
            TeacherRepository.get_by_id(
                db,
                teacher_id,
            )
        )

        if not teacher:

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Teacher not found",
            )

        TeacherRepository.soft_delete(
            db,
            teacher,
        )

        return {
            "message":
            "Teacher deleted successfully"
        }

    @staticmethod
    def map_teacher_section(
        db: Session,
        payload,
    ):

        teacher = (
            TeacherRepository.get_by_id(
                db,
                payload.teacher_id,
            )
        )

        if not teacher:

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Teacher not found",
            )

        section = (
            SectionRepository.get_by_id(
                db,
                payload.section_id,
            )
        )

        if not section:

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Section not found",
            )

        return (
            TeacherRepository.create_teacher_section_mapping(
                db,
                payload.model_dump(),
            )
        )