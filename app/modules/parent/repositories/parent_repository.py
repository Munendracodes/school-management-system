from uuid import UUID

from sqlalchemy import (
    select,
)

from sqlalchemy.orm import (
    Session,
    selectinload,
)

from app.modules.parent.models.parent_model import (
    Parent,
)

from app.modules.student_parent_map.models.student_parent_map_model import (
    StudentParentMap,
)

from app.modules.student.models.student_model import (
    Student,
)

from app.modules.section.models.section_model import (
    Section,
)

from app.modules.classroom.models.classroom_model import (
    Classroom,
)


class ParentRepository:

    @staticmethod
    def create(
        db: Session,
        payload: dict,
    ):

        parent = Parent(
            **payload
        )

        db.add(
            parent
        )

        db.commit()

        db.refresh(
            parent
        )

        return parent

    @staticmethod
    def get_all(
        db: Session,
    ):

        query = (
            select(
                Parent
            )

            .options(

                selectinload(
                    Parent.student_mappings
                )

                .selectinload(
                    StudentParentMap.student
                )

                .selectinload(
                    Student.section
                )

                .selectinload(
                    Section.classroom
                )

                .selectinload(
                    Classroom.academic_year
                )
            )

            .where(
                Parent.is_deleted.is_(
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
        parent_id: UUID,
    ):

        query = (
            select(
                Parent
            )

            .options(

                selectinload(
                    Parent.student_mappings
                )

                .selectinload(
                    StudentParentMap.student
                )

                .selectinload(
                    Student.section
                )

                .selectinload(
                    Section.classroom
                )

                .selectinload(
                    Classroom.academic_year
                )
            )

            .where(
                Parent.id == parent_id,
                Parent.is_deleted.is_(
                    False
                )
            )
        )

        return db.scalar(
            query
        )

    @staticmethod
    def update(
        db: Session,
        parent: Parent,
        payload: dict,
    ):

        for key, value in payload.items():

            setattr(
                parent,
                key,
                value,
            )

        db.commit()

        db.refresh(
            parent
        )

        return parent

    @staticmethod
    def soft_delete(
        db: Session,
        parent: Parent,
    ):

        parent.is_deleted = True

        db.commit()