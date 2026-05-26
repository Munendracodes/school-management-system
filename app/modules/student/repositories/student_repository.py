from uuid import UUID

from sqlalchemy import (
    select,
)

from sqlalchemy.orm import (
    Session,
    selectinload,
)

from app.modules.student.models.student_model import (
    Student,
)

from app.modules.student_parent_map.models.student_parent_map_model import (
    StudentParentMap,
)

from app.modules.section.models.section_model import (
    Section,
)

from app.modules.classroom.models.classroom_model import (
    Classroom,
)

from sqlalchemy import (
    select,
    func,
)


class StudentRepository:

    @staticmethod
    def create(
        db: Session,
        payload: dict,
    ):

        student = Student(
            **payload
        )

        db.add(
            student
        )

        db.commit()

        db.refresh(
            student
        )

        return student

    @staticmethod
    def get_all(
        db: Session,
    ):

        query = (
            select(Student)

            .options(

                selectinload(
                    Student.section
                )

                .selectinload(
                    Section.classroom
                )

                .selectinload(
                    Classroom.academic_year
                ),

                selectinload(
                    Student.parent_mappings
                )

                .selectinload(
                    StudentParentMap.parent
                )
            )

            .where(
                Student.is_deleted.is_(
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
        student_id: UUID,
    ):

        query = (
            select(Student)

            .options(

                selectinload(
                    Student.section
                )

                .selectinload(
                    Section.classroom
                )

                .selectinload(
                    Classroom.academic_year
                ),

                selectinload(
                    Student.parent_mappings
                )

                .selectinload(
                    StudentParentMap.parent
                )
            )

            .where(
                Student.id == student_id,
                Student.is_deleted.is_(
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
        student: Student,
        payload: dict,
    ):

        for key, value in payload.items():

            setattr(
                student,
                key,
                value,
            )

        db.commit()

        db.refresh(
            student
        )

        return student
    
    @staticmethod
    def get_count(
        db: Session,
    ) -> int:

        query = (
            select(
                func.count(
                    Student.id
                )
            )

            .where(
                Student.is_deleted.is_(
                    False
                )
            )
        )

        return db.scalar(
            query
        ) or 0

    @staticmethod
    def soft_delete(
        db: Session,
        student: Student,
    ):

        student.is_deleted = True

        db.commit()