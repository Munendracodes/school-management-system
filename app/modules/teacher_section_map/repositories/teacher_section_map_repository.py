from sqlalchemy import (
    select,
)

from sqlalchemy.orm import (
    Session,
    selectinload,
)

from app.modules.teacher_section_map.models.teacher_section_map_model import (
    TeacherSectionMap,
)

from app.modules.section.models.section_model import (
    Section,
)

from app.modules.classroom.models.classroom_model import (
    Classroom,
)


class TeacherSectionMapRepository:

    @staticmethod
    def create(
        db: Session,
        payload: dict,
    ):

        mapping = TeacherSectionMap(
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
    def get_all(
        db: Session,
    ):

        query = (
            select(
                TeacherSectionMap
            )

            .options(

                selectinload(
                    TeacherSectionMap.teacher
                ),

                selectinload(
                    TeacherSectionMap.section
                )

                .selectinload(
                    Section.classroom
                )

                .selectinload(
                    Classroom.academic_year
                )
            )

            .where(
                TeacherSectionMap.is_deleted.is_(
                    False
                )
            )
        )

        return db.scalars(
            query
        ).all()

    @staticmethod
    def get_by_id(
        db: Session,
        mapping_id,
    ):

        query = (
            select(
                TeacherSectionMap
            )

            .where(
                TeacherSectionMap.id == mapping_id,
                TeacherSectionMap.is_deleted.is_(
                    False
                )
            )
        )

        return db.scalar(
            query
        )

    @staticmethod
    def exists(
        db: Session,
        teacher_id,
        section_id,
        subject_name,
    ):

        query = (
            select(
                TeacherSectionMap
            )
            .where(
                TeacherSectionMap.teacher_id == teacher_id,
                TeacherSectionMap.section_id == section_id,
                TeacherSectionMap.subject_name == subject_name,
                TeacherSectionMap.is_deleted.is_(False),
            )
        )

        return db.scalar(
            query
        )

    @staticmethod
    def soft_delete(
        db: Session,
        mapping,
    ):

        mapping.is_deleted = True

        db.commit()