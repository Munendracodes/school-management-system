from app.modules.homepage.dto.homepage_response_builder import (
    HomepageResponseBuilder,
)

from app.modules.homepage.repositories.homepage_repository import (
    HomepageRepository,
)

from app.modules.dashboard.services.dashboard_service import (
    DashboardService,
)


class StudentHomepageBuilder:

    @staticmethod
    def build(
        db,
        current_user,
    ):

        dashboard = DashboardService.get_student_dashboard(
            db,
            current_user.id,
        )

        widgets = HomepageRepository.get_active_widgets_by_role(
            db,
            role_name="STUDENT",
        )

        branding = {
            "school_name": "Springfield Public School",
            "logo_url": "",
            "primary_color": "#1E3A8A",
        }

        quick_actions = []

        pending_tasks = []

        return HomepageResponseBuilder.build(
            user={
                "id": str(current_user.id),
                "full_name": current_user.full_name,
                "role": current_user.role.name,
            },
            branding=branding,
            dashboard=dashboard,
            widgets=widgets,
            quick_actions=quick_actions,
            pending_tasks=pending_tasks,
        )