from app.modules.dashboard.repositories.dashboard_repository import (
    DashboardRepository,
)


class DashboardService:

    @staticmethod
    def get_admin_summary(
        db,
    ):
        return {
            "total_students": DashboardRepository.get_total_students(db),
            "total_teachers": DashboardRepository.get_total_teachers(db),
            "total_sections": DashboardRepository.get_total_sections(db),
            "total_classrooms": DashboardRepository.get_total_classrooms(db),
        }

    @staticmethod
    def get_attendance_summary(
        db,
    ):
        present = DashboardRepository.get_attendance_count_by_status(
            db,
            "PRESENT",
        ) or  0

        absent = DashboardRepository.get_attendance_count_by_status(
            db,
            "ABSENT",
        )

        leave = DashboardRepository.get_attendance_count_by_status(
            db,
            "LEAVE",
        )

        half_day = DashboardRepository.get_attendance_count_by_status(
            db,
            "HALF_DAY",
        )

        total = DashboardRepository.get_total_today_attendance(
            db,
        ) or 0

        attendance_percentage = 0.0

        if total > 0:
            attendance_percentage = round(
                (present / total) * 100,
                2,
            )

        return {
            "present": present,
            "absent": absent,
            "leave": leave,
            "half_day": half_day,
            "attendance_percentage": attendance_percentage,
        }

    @staticmethod
    def get_teacher_dashboard(
        db,
        teacher_id,
    ):
        assigned_sections = (
            DashboardRepository.get_teacher_assigned_sections(
                db,
                teacher_id,
            )
        )

        students_count = (
            DashboardRepository.get_teacher_students_count(
                db,
                teacher_id,
            )
        )

        attendance_pending = students_count == 0

        return {
            "assigned_sections": assigned_sections,
            "students_count": students_count,
            "attendance_pending": attendance_pending,
        }