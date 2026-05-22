from app.modules.dashboard.repositories.dashboard_repository import (
    DashboardRepository,
)


class DashboardService:

    @staticmethod
    def get_admin_dashboard(
        db,
    ):

        summary = DashboardService.get_admin_summary(
            db,
        )

        attendance = (
            DashboardService.get_attendance_summary(
                db,
            )
        )

        return {
            **summary,
            "attendance": attendance,
        }

    @staticmethod
    def get_admin_summary(
        db,
    ):

        return {
            "total_students": (
                DashboardRepository.get_total_students(
                    db,
                ) or 0
            ),

            "total_teachers": (
                DashboardRepository.get_total_teachers(
                    db,
                ) or 0
            ),

            "total_sections": (
                DashboardRepository.get_total_sections(
                    db,
                ) or 0
            ),

            "total_classrooms": (
                DashboardRepository.get_total_classrooms(
                    db,
                ) or 0
            ),
        }

    @staticmethod
    def get_attendance_summary(
        db,
    ):

        present = (
            DashboardRepository.get_attendance_count_by_status(
                db,
                "PRESENT",
            ) or 0
        )

        absent = (
            DashboardRepository.get_attendance_count_by_status(
                db,
                "ABSENT",
            ) or 0
        )

        leave = (
            DashboardRepository.get_attendance_count_by_status(
                db,
                "LEAVE",
            ) or 0
        )

        half_day = (
            DashboardRepository.get_attendance_count_by_status(
                db,
                "HALF_DAY",
            ) or 0
        )

        total = (
            DashboardRepository.get_total_today_attendance(
                db,
            ) or 0
        )

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
            "total": total,
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

        attendance_pending = (
            students_count > 0
        )

        return {
            "assigned_sections": assigned_sections,
            "students_count": students_count,
            "attendance_pending": attendance_pending,
        }

    @staticmethod
    def get_student_dashboard(
        db,
        student_id,
    ):

        attendance_summary = (
            DashboardRepository.get_student_attendance_summary(
                db,
                student_id,
            )
        )

        return {
            "attendance": attendance_summary,
        }

    @staticmethod
    def get_parent_dashboard(
        db,
        parent_id,
    ):

        children = (
            DashboardRepository.get_parent_children(
                db,
                parent_id,
            )
        )

        return {
            "children_count": len(children),
            "children": children,
        }