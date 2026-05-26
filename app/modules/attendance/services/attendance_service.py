from fastapi import (
    HTTPException,
    status,
)

from sqlalchemy.orm import Session

from app.modules.attendance.repositories.attendance_repository import (
    AttendanceRepository,
)

from app.modules.student.repositories.student_repository import (
    StudentRepository,
)

from app.modules.teacher.repositories.teacher_repository import (
    TeacherRepository,
)


class AttendanceService:

    @staticmethod
    def create_attendance(
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

        teacher = TeacherRepository.get_by_id(
            db,
            payload.teacher_id,
        )

        if not teacher:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Teacher not found",
            )

        valid_statuses = [
            "PRESENT",
            "ABSENT",
            "HALF_DAY",
            "LEAVE",
        ]

        if payload.status not in valid_statuses:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid attendance status",
            )

        return AttendanceRepository.create(
            db,
            payload.model_dump(),
        )

    @staticmethod
    def get_attendance(
        db: Session,
    ):

        return AttendanceRepository.get_all(
            db
        )

    @staticmethod
    def get_attendance_by_student(
        db: Session,
        student_id,
    ):

        return AttendanceRepository.get_by_student(
            db,
            student_id,
        )

    @staticmethod
    def update_attendance(
        db: Session,
        attendance_id,
        payload,
    ):

        attendance = AttendanceRepository.get_by_id(
            db,
            attendance_id,
        )

        if not attendance:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Attendance not found",
            )

        return AttendanceRepository.update(
            db,
            attendance,
            payload.model_dump(
                exclude_unset=True,
            ),
        )

    @staticmethod
    def delete_attendance(
        db: Session,
        attendance_id,
    ):

        attendance = AttendanceRepository.get_by_id(
            db,
            attendance_id,
        )

        if not attendance:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Attendance not found",
            )

        AttendanceRepository.soft_delete(
            db,
            attendance,
        )

        return {
            "message":
            "Attendance deleted successfully"
        }