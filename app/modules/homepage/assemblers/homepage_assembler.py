from app.modules.homepage.builders.admin_homepage_builder import (
    AdminHomepageBuilder,
)

from app.modules.homepage.builders.teacher_homepage_builder import (
    TeacherHomepageBuilder,
)

from app.modules.homepage.builders.student_homepage_builder import (
    StudentHomepageBuilder,
)

from app.modules.homepage.builders.parent_homepage_builder import (
    ParentHomepageBuilder,
)


class HomepageAssembler:

    @staticmethod
    def build(
        db,
        current_user,
    ):

        role_name = current_user.role.name

        if role_name == "SUPER_ADMIN":
            return AdminHomepageBuilder.build(
                db,
                current_user,
            )

        if role_name == "ADMIN":
            return AdminHomepageBuilder.build(
                db,
                current_user,
            )

        if role_name == "TEACHER":
            return TeacherHomepageBuilder.build(
                db,
                current_user,
            )

        if role_name == "STUDENT":
            return StudentHomepageBuilder.build(
                db,
                current_user,
            )

        if role_name == "PARENT":
            return ParentHomepageBuilder.build(
                db,
                current_user,
            )

        return {
            "message": "No homepage available for role",
        }