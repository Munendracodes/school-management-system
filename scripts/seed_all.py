from datetime import date, timedelta
from random import choice
import traceback
import csv

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from app.database.session import SessionLocal

from app.modules.users.models.role_model import (
    RoleModel as Role,
)

from app.modules.users.models.user_model import (
    UserModel,
)

from app.modules.academic_year.models.academic_year_model import (
    AcademicYear,
)

from app.modules.classroom.models.classroom_model import (
    ClassRoom,
)

from app.modules.section.models.section_model import (
    Section,
)

from app.modules.teacher.models.teacher_model import (
    Teacher,
)

from app.modules.student.models.student_model import (
    Student,
)

from app.modules.parent.models.parent_model import (
    Parent,
)

from app.modules.parent.models.student_parent_mapping_model import (
    StudentParentMapping,
)

from app.modules.teacher.models.teacher_section_mapping_model import (
    TeacherSectionMapping,
)

from app.modules.attendance.models.attendance_model import (
    Attendance,
)

from app.modules.homepage.models.homepage_widget_model import (
    HomepageWidget,
)

from app.modules.users.utils.password_handler import (
    hash_password,
)


db = SessionLocal()

csv_rows = []


def log_info(message):
    print(f"ℹ️  {message}")


def log_success(message):
    print(f"✅ {message}")


def log_warning(message):
    print(f"⚠️  {message}")


def log_error(message):
    print(f"❌ {message}")


def log_section(title):

    print()
    print("=" * 80)
    print(f"🚀 {title}")
    print("=" * 80)


def add_csv_row(
    module,
    name,
    status,
    remarks="",
):

    csv_rows.append({
        "module": module,
        "name": name,
        "status": status,
        "remarks": remarks,
    })


ROLES = [
    "SUPER_ADMIN",
    "ADMIN",
    "TEACHER",
    "STUDENT",
    "PARENT",
]


def create_roles():

    log_section("CREATING ROLES")

    for role_name in ROLES:

        existing = db.scalar(
            select(Role).where(
                Role.name == role_name,
            )
        )

        if existing:

            log_warning(
                f"Role already exists -> {role_name}"
            )

            add_csv_row(
                "ROLE",
                role_name,
                "EXISTS",
            )

            continue

        role = Role(
            name=role_name,
            description=f"{role_name} Role",
        )

        db.add(role)

        db.commit()

        log_success(
            f"Created role -> {role_name}"
        )

        add_csv_row(
            "ROLE",
            role_name,
            "CREATED",
        )


def create_super_admin():

    log_section(
        "CREATING SUPER ADMIN"
    )

    existing = db.scalar(
        select(UserModel).where(
            UserModel.mobile_number
            == "9999999999",
        )
    )

    if existing:

        log_warning(
            "Super admin already exists"
        )

        add_csv_row(
            "USER",
            "Super Admin",
            "EXISTS",
        )

        return existing

    role = db.scalar(
        select(Role).where(
            Role.name == "SUPER_ADMIN",
        )
    )

    user = UserModel(
        full_name="Super Admin",
        mobile_number="9999999999",
        email="superadmin@school.com",
        password_hash=hash_password("1234"),
        role_id=role.id,
        is_active=True,
        is_first_login=False,
    )

    db.add(user)

    db.commit()

    db.refresh(user)

    log_success(
        "Created super admin"
    )

    add_csv_row(
        "USER",
        "Super Admin",
        "CREATED",
    )

    return user


def create_admin():

    log_section("CREATING ADMIN")

    existing = db.scalar(
        select(UserModel).where(
            UserModel.mobile_number
            == "8888888888",
        )
    )

    if existing:

        log_warning(
            "Admin already exists"
        )

        add_csv_row(
            "USER",
            "Admin",
            "EXISTS",
        )

        return existing

    role = db.scalar(
        select(Role).where(
            Role.name == "ADMIN",
        )
    )

    user = UserModel(
        full_name="Main Admin",
        mobile_number="8888888888",
        email="admin@school.com",
        password_hash=hash_password("1234"),
        role_id=role.id,
        is_active=True,
        is_first_login=False,
    )

    db.add(user)

    db.commit()

    db.refresh(user)

    log_success(
        "Created admin"
    )

    add_csv_row(
        "USER",
        "Main Admin",
        "CREATED",
    )

    return user


def create_academic_year():

    log_section(
        "CREATING ACADEMIC YEAR"
    )

    existing = db.scalar(
        select(AcademicYear).where(
            AcademicYear.name == "2025-2026",
        )
    )

    if existing:

        log_warning(
            "Academic year already exists"
        )

        add_csv_row(
            "ACADEMIC_YEAR",
            "2025-2026",
            "EXISTS",
        )

        return existing

    academic_year = AcademicYear(
        name="2025-2026",
        start_date=date(2025, 6, 1),
        end_date=date(2026, 4, 30),
        is_active=True,
    )

    db.add(academic_year)

    db.commit()

    db.refresh(academic_year)

    log_success(
        "Created academic year"
    )

    add_csv_row(
        "ACADEMIC_YEAR",
        "2025-2026",
        "CREATED",
    )

    return academic_year


def create_classrooms(
    academic_year,
):

    log_section(
        "CREATING CLASSROOMS"
    )

    classrooms = []

    for index, name in enumerate(
        ["Class 1", "Class 2"],
        start=1,
    ):

        existing = db.scalar(
            select(ClassRoom).where(
                ClassRoom.name == name,
            )
        )

        if existing:

            log_warning(
                f"Classroom exists -> {name}"
            )

            classrooms.append(existing)

            add_csv_row(
                "CLASSROOM",
                name,
                "EXISTS",
            )

            continue

        classroom = ClassRoom(
            name=name,
            display_order=index,
            academic_year_id=academic_year.id,
            is_active=True,
        )

        db.add(classroom)

        db.commit()

        db.refresh(classroom)

        classrooms.append(classroom)

        log_success(
            f"Created classroom -> {name}"
        )

        add_csv_row(
            "CLASSROOM",
            name,
            "CREATED",
        )

    return classrooms


def create_sections(
    classrooms,
):

    log_section(
        "CREATING SECTIONS"
    )

    sections = []

    display_order = 1

    for classroom in classrooms:

        for name in ["A", "B"]:

            existing = db.scalar(
                select(Section).where(
                    Section.name == name,
                    Section.classroom_id
                    == classroom.id,
                )
            )

            if existing:

                sections.append(existing)

                log_warning(
                    f"Section exists -> "
                    f"{classroom.name}-{name}"
                )

                add_csv_row(
                    "SECTION",
                    f"{classroom.name}-{name}",
                    "EXISTS",
                )

                continue

            section = Section(
                name=name,
                classroom_id=classroom.id,
                capacity=40,
                display_order=display_order,
                is_active=True,
            )

            db.add(section)

            db.commit()

            db.refresh(section)

            sections.append(section)

            log_success(
                f"Created section -> "
                f"{classroom.name}-{name}"
            )

            add_csv_row(
                "SECTION",
                f"{classroom.name}-{name}",
                "CREATED",
            )

            display_order += 1

    return sections


def create_teachers():

    log_section(
        "CREATING TEACHERS"
    )

    teachers = []

    data = [
        {
            "employee_id": "EMP001",
            "full_name": "Ravi Kumar",
            "gender": "MALE",
            "mobile_number": "9000000001",
            "email": "ravi@school.com",
            "qualification": "M.Sc Maths",
            "experience_years": 5,
        },
        {
            "employee_id": "EMP002",
            "full_name": "Priya Sharma",
            "gender": "FEMALE",
            "mobile_number": "9000000002",
            "email": "priya@school.com",
            "qualification": "M.A English",
            "experience_years": 4,
        },
    ]

    for item in data:

        existing = db.scalar(
            select(Teacher).where(
                Teacher.employee_id
                == item["employee_id"],
            )
        )

        if existing:

            teachers.append(existing)

            log_warning(
                f"Teacher exists -> "
                f"{item['full_name']}"
            )

            add_csv_row(
                "TEACHER",
                item["full_name"],
                "EXISTS",
            )

            continue

        teacher = Teacher(
            employee_id=item["employee_id"],
            full_name=item["full_name"],
            gender=item["gender"],
            mobile_number=item["mobile_number"],
            email=item["email"],
            qualification=item["qualification"],
            experience_years=item["experience_years"],
            joining_date=date.today(),
            is_class_teacher=True,
            is_active=True,
        )

        db.add(teacher)

        db.commit()

        db.refresh(teacher)

        teachers.append(teacher)

        log_success(
            f"Created teacher -> "
            f"{teacher.full_name}"
        )

        add_csv_row(
            "TEACHER",
            teacher.full_name,
            "CREATED",
        )

    return teachers


def assign_teachers_to_sections(
    teachers,
    sections,
):

    log_section(
        "ASSIGNING TEACHERS TO SECTIONS"
    )

    subjects = [
        "Mathematics",
        "English",
        "Science",
        "Social",
    ]

    for index, section in enumerate(sections):

        teacher = teachers[
            index % len(teachers)
        ]

        existing = db.scalar(
            select(TeacherSectionMapping).where(
                TeacherSectionMapping.teacher_id
                == teacher.id,
                TeacherSectionMapping.section_id
                == section.id,
            )
        )

        if existing:

            log_warning(
                f"Mapping exists -> "
                f"{teacher.full_name}"
            )

            add_csv_row(
                "TEACHER_MAPPING",
                teacher.full_name,
                "EXISTS",
            )

            continue

        mapping = TeacherSectionMapping(
            teacher_id=teacher.id,
            section_id=section.id,
            subject_name=subjects[index],
            is_class_teacher=True,
        )

        db.add(mapping)

        db.commit()

        log_success(
            f"Mapped teacher -> "
            f"{teacher.full_name}"
        )

        add_csv_row(
            "TEACHER_MAPPING",
            teacher.full_name,
            "CREATED",
        )


def create_students_and_parents(
    sections,
    academic_year,
):

    log_section(
        "CREATING STUDENTS & PARENTS"
    )

    students = []

    parent_counter = 1

    for section in sections:

        current_parent = None

        for i in range(1, 6):

            admission_number = (
                f"ADM-{section.name}-{i}"
            )

            existing = db.scalar(
                select(Student).where(
                    Student.admission_number
                    == admission_number,
                )
            )

            if existing:

                students.append(existing)

                log_warning(
                    f"Student exists -> "
                    f"{admission_number}"
                )

                add_csv_row(
                    "STUDENT",
                    admission_number,
                    "EXISTS",
                )

                continue

            student = Student(
                admission_number=admission_number,
                full_name=f"{section.name} Student {i}",
                gender=choice(
                    ["MALE", "FEMALE"]
                ),
                date_of_birth=date(2015, 6, i),
                mobile_number=f"8000000{i}",
                email=f"student{i}@school.com",
                address="West Mambalam, Chennai",
                guardian_name=f"Parent {parent_counter}",
                guardian_mobile_number=(
                    f"7000000{parent_counter}"
                ),
                academic_year_id=academic_year.id,
                classroom_id=section.classroom_id,
                section_id=section.id,
                roll_number=f"ROLL-{i}",
                admission_date=date.today(),
                is_active=True,
            )

            db.add(student)

            db.commit()

            db.refresh(student)

            students.append(student)

            log_success(
                f"Created student -> "
                f"{student.full_name}"
            )

            add_csv_row(
                "STUDENT",
                student.full_name,
                "CREATED",
            )

            if i % 2 != 0:

                parent = Parent(
                    father_name=f"Father {i}",
                    mother_name=f"Mother {i}",
                    guardian_name=f"Parent {i}",
                    mobile_number=(
                        f"7000000{parent_counter}"
                    ),
                    alternate_mobile_number=(
                        f"7111111{parent_counter}"
                    ),
                    email=f"parent{i}@gmail.com",
                    occupation="Engineer",
                    address="Chennai",
                    is_active=True,
                )

                db.add(parent)

                db.commit()

                db.refresh(parent)

                current_parent = parent

                log_success(
                    f"Created parent -> "
                    f"{parent.guardian_name}"
                )

                add_csv_row(
                    "PARENT",
                    parent.guardian_name,
                    "CREATED",
                )

                parent_counter += 1

            if current_parent:

                mapping_exists = db.scalar(
                    select(StudentParentMapping).where(
                        StudentParentMapping.student_id
                        == student.id,
                        StudentParentMapping.parent_id
                        == current_parent.id,
                    )
                )

                if not mapping_exists:

                    mapping = StudentParentMapping(
                        student_id=student.id,
                        parent_id=current_parent.id,
                        relationship_type="FATHER",
                    )

                    db.add(mapping)

                    db.commit()

                    log_info(
                        f"Mapped student "
                        f"{student.full_name}"
                    )

                    add_csv_row(
                        "PARENT_MAPPING",
                        student.full_name,
                        "CREATED",
                    )

    return students


def create_attendance(
    students,
    teachers,
):

    log_section(
        "CREATING ATTENDANCE"
    )

    statuses = [
        "PRESENT",
        "ABSENT",
        "HALF_DAY",
        "LEAVE",
    ]

    count = 0

    for student in students:

        for day in range(1, 8):

            attendance_date = (
                date.today()
                - timedelta(days=day)
            )

            existing = db.scalar(
                select(Attendance).where(
                    Attendance.student_id
                    == student.id,
                    Attendance.attendance_date
                    == attendance_date,
                )
            )

            if existing:
                continue

            attendance = Attendance(
                student_id=student.id,
                section_id=student.section_id,
                teacher_id=teachers[0].id,
                attendance_date=attendance_date,
                status=choice(statuses),
                remarks="Auto generated attendance",
            )

            db.add(attendance)

            count += 1

    db.commit()

    log_success(
        f"Created attendance records -> "
        f"{count}"
    )

    add_csv_row(
        "ATTENDANCE",
        "Attendance Records",
        "CREATED",
        f"{count} records",
    )


def create_homepage_widgets():

    log_section(
        "CREATING HOMEPAGE WIDGETS"
    )

    widgets = [
        {
            "title": "Admissions Open",
            "widget_type": "BANNER",
            "roles": ["ADMIN"],
        },
        {
            "title": "Attendance Summary",
            "widget_type": "ATTENDANCE",
            "roles": ["TEACHER"],
        },
        {
            "title": "Homework Reminder",
            "widget_type": "HOMEWORK",
            "roles": ["STUDENT"],
        },
    ]

    for item in widgets:

        existing = db.scalar(
            select(HomepageWidget).where(
                HomepageWidget.title
                == item["title"],
            )
        )

        if existing:

            log_warning(
                f"Widget exists -> "
                f"{item['title']}"
            )

            continue

        widget = HomepageWidget(
            title=item["title"],
            widget_type=item["widget_type"],
            subtitle="Dynamic Homepage Widget",
            image_url=(
                "https://images.unsplash.com/"
                "photo-1509062522246-3755977927d7"
            ),
            redirect_url="/dashboard",
            sequence=1,
            visibility_roles=item["roles"],
            config_json={},
            is_active=True,
        )

        db.add(widget)

        db.commit()

        log_success(
            f"Created widget -> "
            f"{item['title']}"
        )

        add_csv_row(
            "WIDGET",
            item["title"],
            "CREATED",
        )


def export_csv():

    filename = "seed_report.csv"

    with open(
        filename,
        "w",
        newline="",
        encoding="utf-8",
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "module",
                "name",
                "status",
                "remarks",
            ],
        )

        writer.writeheader()

        writer.writerows(csv_rows)

    log_success(
        f"CSV report generated -> "
        f"{filename}"
    )


def run():

    try:

        log_section(
            "STARTING FULL DATABASE SEED"
        )

        create_roles()

        create_super_admin()

        create_admin()

        academic_year = (
            create_academic_year()
        )

        classrooms = create_classrooms(
            academic_year,
        )

        sections = create_sections(
            classrooms,
        )

        teachers = create_teachers()

        assign_teachers_to_sections(
            teachers,
            sections,
        )

        students = (
            create_students_and_parents(
                sections,
                academic_year,
            )
        )

        create_attendance(
            students,
            teachers,
        )

        create_homepage_widgets()

        export_csv()

        print()
        print("🎉" * 20)

        log_success(
            "FULL DATABASE SEED COMPLETED"
        )

        print("🎉" * 20)

    except SQLAlchemyError as error:

        db.rollback()

        log_error(
            "DATABASE ERROR OCCURRED"
        )

        log_error(str(error))

        traceback.print_exc()

    except Exception as error:

        db.rollback()

        log_error(
            "UNEXPECTED ERROR OCCURRED"
        )

        log_error(str(error))

        traceback.print_exc()

    finally:

        db.close()

        log_info(
            "Database session closed"
        )


if __name__ == "__main__":

    run()