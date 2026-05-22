# from app.modules.users.models import User
from app.modules.settings.models import SchoolSettings
from app.modules.users.models import (
    RoleModel,
    UserModel,
)
from app.modules.academic_year.models.academic_year_model import AcademicYear
from app.modules.classroom.models.classroom_model import ClassRoom
from app.modules.section.models.section_model import Section
from app.modules.student.models.student_model import Student
from app.modules.parent.models.parent_model import Parent
from app.modules.parent.models.student_parent_mapping_model import (
    StudentParentMapping,
)
from app.modules.teacher.models.teacher_model import Teacher

from app.modules.teacher.models.teacher_section_mapping_model import (
    TeacherSectionMapping,
)
from app.modules.attendance.models.attendance_model import Attendance
from app.modules.homepage.models.homepage_widget_model import (
    HomepageWidget,
)