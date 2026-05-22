from datetime import date

from sqlalchemy import (
    select,
    func,
)

from app.modules.student.models.student_model import Student

from app.modules.teacher.models.teacher_model import Teacher

from app.modules.section.models.section_model import Section

from app.modules.classroom.models.classroom_model import (
    ClassRoom,
)

from app.modules.attendance.models.attendance_model import Attendance

from app.modules.teacher.models.teacher_section_mapping_model import (
    TeacherSectionMapping,
)

from sqlalchemy import (
    select,
    func,
)

from app.modules.attendance.models.attendance_model import (
    Attendance,
)

from app.modules.student.models.student_model import (
    Student,
)

from app.modules.parent.models.student_parent_mapping_model import (
    StudentParentMapping,
)


class DashboardQueries:

    @staticmethod
    def total_students():
        return select(
            func.count(Student.id)
        ).where(
            Student.is_deleted == False,
        )

    @staticmethod
    def total_teachers():
        return select(
            func.count(Teacher.id)
        ).where(
            Teacher.is_deleted == False,
        )

    @staticmethod
    def total_sections():
        return select(
            func.count(Section.id)
        ).where(
            Section.is_deleted == False,
        )

    @staticmethod
    def total_classrooms():
        return select(
            func.count(ClassRoom.id)
        ).where(
            ClassRoom.is_deleted == False,
        )

    @staticmethod
    def attendance_count_by_status(
        attendance_status: str,
    ):
        return select(
            func.count(Attendance.id)
        ).where(
            Attendance.status == attendance_status,
            Attendance.attendance_date == date.today(),
            Attendance.is_deleted == False,
        )

    @staticmethod
    def total_today_attendance():
        return select(
            func.count(Attendance.id)
        ).where(
            Attendance.attendance_date == date.today(),
            Attendance.is_deleted == False,
        )

    @staticmethod
    def teacher_assigned_sections(
        teacher_id,
    ):
        return select(
            func.count(TeacherSectionMapping.id)
        ).where(
            TeacherSectionMapping.teacher_id == teacher_id,
            TeacherSectionMapping.is_deleted == False,
        )

    @staticmethod
    def teacher_students_count(
        teacher_id,
    ):
        return (
            select(
                func.count(Student.id)
            )
            .join(
                Section,
                Student.section_id == Section.id,
            )
            .join(
                TeacherSectionMapping,
                TeacherSectionMapping.section_id == Section.id,
            )
            .where(
                TeacherSectionMapping.teacher_id == teacher_id,
                Student.is_deleted == False,
            )
        )
    
    @staticmethod
    def student_attendance_summary(
        student_id,
    ):

        total_subquery = (
            select(
                func.count(Attendance.id)
            )
            .where(
                Attendance.student_id == student_id,
                Attendance.is_deleted == False,
            )
            .scalar_subquery()
        )

        present_subquery = (
            select(
                func.count(Attendance.id)
            )
            .where(
                Attendance.student_id == student_id,
                Attendance.status == "PRESENT",
                Attendance.is_deleted == False,
            )
            .scalar_subquery()
        )

        return select(
            total_subquery.label("total"),
            present_subquery.label("present"),
        )
    
    @staticmethod
    def parent_children(
        parent_id,
    ):

        return (
            select(
                Student.id,
                Student.full_name,
            )
            .join(
                StudentParentMapping,
                Student.id == StudentParentMapping.student_id,
            )
            .where(
                StudentParentMapping.parent_id == parent_id,
                Student.is_deleted == False,
            )
        )