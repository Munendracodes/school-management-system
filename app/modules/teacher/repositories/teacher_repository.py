from sqlalchemy import select
from sqlalchemy.orm import Session

from app.modules.teacher.models.teacher_model import Teacher

from app.modules.teacher.models.teacher_section_mapping_model import (
    TeacherSectionMapping,
)


class TeacherRepository:

    @staticmethod
    def create(
        db: Session,
        payload: dict,
    ):
        teacher = Teacher(**payload)

        db.add(teacher)

        db.commit()
        db.refresh(teacher)

        return teacher

    @staticmethod
    def get_all(
        db: Session,
    ):
        query = select(Teacher).where(
            Teacher.is_deleted == False,
        )

        return db.scalars(query).all()

    @staticmethod
    def get_by_id(
        db: Session,
        teacher_id: str,
    ):
        query = select(Teacher).where(
            Teacher.id == teacher_id,
            Teacher.is_deleted == False,
        )

        return db.scalar(query)

    @staticmethod
    def get_by_employee_id(
        db: Session,
        employee_id: str,
    ):
        query = select(Teacher).where(
            Teacher.employee_id == employee_id,
            Teacher.is_deleted == False,
        )

        return db.scalar(query)

    @staticmethod
    def get_by_mobile_number(
        db: Session,
        mobile_number: str,
    ):
        query = select(Teacher).where(
            Teacher.mobile_number == mobile_number,
            Teacher.is_deleted == False,
        )

        return db.scalar(query)

    @staticmethod
    def update(
        db: Session,
        teacher: Teacher,
        payload: dict,
    ):
        for key, value in payload.items():
            setattr(teacher, key, value)

        db.commit()
        db.refresh(teacher)

        return teacher

    @staticmethod
    def soft_delete(
        db: Session,
        teacher: Teacher,
    ):
        teacher.is_deleted = True

        db.commit()

    @staticmethod
    def create_teacher_section_mapping(
        db: Session,
        payload: dict,
    ):
        mapping = TeacherSectionMapping(**payload)

        db.add(mapping)

        db.commit()
        db.refresh(mapping)

        return mapping