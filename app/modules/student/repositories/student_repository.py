from sqlalchemy import select
from sqlalchemy.orm import Session

from app.modules.student.models.student_model import Student


class StudentRepository:

    @staticmethod
    def create(
        db: Session,
        payload: dict,
    ):
        student = Student(**payload)

        db.add(student)

        db.commit()
        db.refresh(student)

        return student

    @staticmethod
    def get_all(
        db: Session,
    ):
        query = select(Student).where(
            Student.is_deleted == False,
        )

        return db.scalars(query).all()

    @staticmethod
    def get_by_id(
        db: Session,
        student_id: str,
    ):
        query = select(Student).where(
            Student.id == student_id,
            Student.is_deleted == False,
        )

        return db.scalar(query)

    @staticmethod
    def get_by_admission_number(
        db: Session,
        admission_number: str,
    ):
        query = select(Student).where(
            Student.admission_number == admission_number,
            Student.is_deleted == False,
        )

        return db.scalar(query)

    @staticmethod
    def update(
        db: Session,
        student: Student,
        payload: dict,
    ):
        for key, value in payload.items():
            setattr(student, key, value)

        db.commit()
        db.refresh(student)

        return student

    @staticmethod
    def soft_delete(
        db: Session,
        student: Student,
    ):
        student.is_deleted = True

        db.commit()