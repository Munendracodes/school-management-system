from pydantic import BaseModel


class AdminSummarySchema(BaseModel):

    total_students: int
    total_teachers: int
    total_sections: int
    total_classrooms: int


class AttendanceSummarySchema(BaseModel):

    present: int
    absent: int
    leave: int
    half_day: int
    attendance_percentage: float


class TeacherDashboardSchema(BaseModel):

    assigned_sections: int
    students_count: int
    attendance_pending: bool