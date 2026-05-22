from sqlalchemy.orm import Session

from app.modules.dashboard.queries.dashboard_queries import (
    DashboardQueries,
)


class DashboardRepository:

    @staticmethod
    def get_total_students(
        db: Session,
    ):
        return db.scalar(
            DashboardQueries.total_students()
        )

    @staticmethod
    def get_total_teachers(
        db: Session,
    ):
        return db.scalar(
            DashboardQueries.total_teachers()
        )

    @staticmethod
    def get_total_sections(
        db: Session,
    ):
        return db.scalar(
            DashboardQueries.total_sections()
        )

    @staticmethod
    def get_total_classrooms(
        db: Session,
    ):
        return db.scalar(
            DashboardQueries.total_classrooms()
        )

    @staticmethod
    def get_attendance_count_by_status(
        db: Session,
        attendance_status: str,
    ):
        return db.scalar(
            DashboardQueries.attendance_count_by_status(
                attendance_status,
            )
        )

    @staticmethod
    def get_total_today_attendance(
        db: Session,
    ):
        return db.scalar(
            DashboardQueries.total_today_attendance()
        )

    @staticmethod
    def get_teacher_assigned_sections(
        db: Session,
        teacher_id,
    ):
        return db.scalar(
            DashboardQueries.teacher_assigned_sections(
                teacher_id,
            )
        )

    @staticmethod
    def get_teacher_students_count(
        db: Session,
        teacher_id,
    ):
        return db.scalar(
            DashboardQueries.teacher_students_count(
                teacher_id,
            )
        )