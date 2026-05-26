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

from app.modules.teacher_section_map.repositories.teacher_section_map_repository import (
    TeacherSectionMapRepository,
)


class TeacherSectionMapService:

    @staticmethod
    def create_mapping(
        db: Session,
        payload,
    ):

        teacher = TeacherRepository.get_by_id(
            db,
            payload.teacher_id,
        )

        if not teacher:

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Teacher not found",
            )

        section = SectionRepository.get_by_id(
            db,
            payload.section_id,
        )

        if not section:

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Section not found",
            )

        exists = (
            TeacherSectionMapRepository.exists(
                db,
                payload.teacher_id,
                payload.section_id,
                payload.subject_name,
            )
        )

        if exists:

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Teacher mapping already exists",
            )

        return (
            TeacherSectionMapRepository.create(
                db,
                payload.model_dump(),
            )
        )

    @staticmethod
    def get_mappings(
        db: Session,
    ):

        return (
            TeacherSectionMapRepository.get_all(
                db
            )
        )

    @staticmethod
    def delete_mapping(
        db: Session,
        mapping_id,
    ):

        mapping = (
            TeacherSectionMapRepository.get_by_id(
                db,
                mapping_id,
            )
        )

        if not mapping:

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Mapping not found",
            )

        TeacherSectionMapRepository.soft_delete(
            db,
            mapping,
        )

        return {
            "message":
            "Teacher mapping deleted successfully"
        }