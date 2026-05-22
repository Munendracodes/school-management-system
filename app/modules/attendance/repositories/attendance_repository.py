from sqlalchemy import select
from sqlalchemy.orm import Session

from app.modules.attendance.models.attendance_model import Attendance


class AttendanceRepository:

    @staticmethod
    def create(
        db: Session,
        payload: dict,
    ):
        attendance = Attendance(**payload)

        db.add(attendance)

        db.commit()
        db.refresh(attendance)

        return attendance

    @staticmethod
    def get_all(
        db: Session,
    ):
        query = select(Attendance).where(
            Attendance.is_deleted == False,
        )

        return db.scalars(query).all()

    @staticmethod
    def get_by_id(
        db: Session,
        attendance_id: str,
    ):
        query = select(Attendance).where(
            Attendance.id == attendance_id,
            Attendance.is_deleted == False,
        )

        return db.scalar(query)

    @staticmethod
    def get_by_student(
        db: Session,
        student_id: str,
    ):
        query = select(Attendance).where(
            Attendance.student_id == student_id,
            Attendance.is_deleted == False,
        )

        return db.scalars(query).all()

    @staticmethod
    def get_by_section(
        db: Session,
        section_id: str,
    ):
        query = select(Attendance).where(
            Attendance.section_id == section_id,
            Attendance.is_deleted == False,
        )

        return db.scalars(query).all()

    @staticmethod
    def update(
        db: Session,
        attendance: Attendance,
        payload: dict,
    ):
        for key, value in payload.items():
            setattr(attendance, key, value)

        db.commit()
        db.refresh(attendance)

        return attendance

    @staticmethod
    def soft_delete(
        db: Session,
        attendance: Attendance,
    ):
        attendance.is_deleted = True

        db.commit()