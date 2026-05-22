from fastapi import (
    HTTPException,
    status,
)

from sqlalchemy.orm import Session

from app.modules.section.repositories.section_repository import (
    SectionRepository,
)

from app.modules.classroom.repositories.classroom_repository import (
    ClassRoomRepository,
)


class SectionService:

    @staticmethod
    def create_section(
        db: Session,
        payload,
    ):
        classroom = ClassRoomRepository.get_by_id(
            db,
            payload.classroom_id,
        )

        if not classroom:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Classroom not found",
            )

        return SectionRepository.create(
            db,
            payload.model_dump(),
        )

    @staticmethod
    def get_sections(
        db: Session,
    ):
        return SectionRepository.get_all(db)

    @staticmethod
    def get_section_by_id(
        db: Session,
        section_id,
    ):
        section = SectionRepository.get_by_id(
            db,
            section_id,
        )

        if not section:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Section not found",
            )

        return section

    @staticmethod
    def update_section(
        db: Session,
        section_id,
        payload,
    ):
        section = SectionRepository.get_by_id(
            db,
            section_id,
        )

        if not section:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Section not found",
            )

        return SectionRepository.update(
            db,
            section,
            payload.model_dump(exclude_unset=True),
        )

    @staticmethod
    def delete_section(
        db: Session,
        section_id,
    ):
        section = SectionRepository.get_by_id(
            db,
            section_id,
        )

        if not section:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Section not found",
            )

        SectionRepository.soft_delete(
            db,
            section,
        )

        return {
            "message": "Section deleted successfully",
        }