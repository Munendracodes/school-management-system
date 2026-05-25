from app.modules.dashboard.services.dashboard_service import (
    DashboardService,
)

from app.modules.homepage.dto.homepage_response_builder import (
    HomepageResponseBuilder,
)

from app.modules.homepage.section_builders.overview_section_builder import (
    OverviewSectionBuilder,
)

from app.modules.homepage.section_builders.quick_actions_section_builder import (
    QuickActionsSectionBuilder,
)

from app.modules.homepage.section_builders.academic_structure_section_builder import (
    AcademicStructureSectionBuilder,
)

from app.modules.homepage.section_builders.student_operations_section_builder import (
    StudentOperationsSectionBuilder,
)

from app.core.utils.datetime_utils import (
    DateTimeUtils,
)




class AdminHomepageBuilder:

    @staticmethod
    def build(
        db,
        current_user,
    ):

        dashboard = DashboardService.get_admin_dashboard(
            db,
        )

        current_hour = DateTimeUtils.current_hour()
        print(f"Current hour: {current_hour}")

        if 6 <= current_hour < 12:
            greeting = "Good Morning"

        elif 12 <= current_hour < 18:
            greeting = "Good Afternoon"

        else:
            greeting = "Good Evening"

        sections = [
            OverviewSectionBuilder.build(
                dashboard,
            ),

            QuickActionsSectionBuilder.build(),

            AcademicStructureSectionBuilder.build(),

            StudentOperationsSectionBuilder.build(),
        ]

        return HomepageResponseBuilder.build(

            user={
                "id": str(current_user.id),
                "full_name": current_user.full_name,
                "role": current_user.role.name,
            },

            header={
                "school_name": "Sunshine Public School",
                "school_logo": "",
                "screen_title": "Admin Dashboard",
                "notification_count": 4,
            },

            hero_banner={
                "title": (
                    f"{greeting}, "
                    f"{current_user.full_name} 👋"
                ),

                "subtitle": (
                    DateTimeUtils.now().strftime(
                        "%A, %d %B %Y"
                    )
                ),

                "image_url": "",
            },

            sections=sections,

            bottom_navigation=[
                {
                    "title": "Home",
                    "icon": "home",
                    "redirect_url": "/home",
                },
                {
                    "title": "Manage",
                    "icon": "manage",
                    "redirect_url": "/manage",
                },
                {
                    "title": "Reports",
                    "icon": "reports",
                    "redirect_url": "/reports",
                },
                {
                    "title": "More",
                    "icon": "more",
                    "redirect_url": "/more",
                },
            ],

            meta={
                "homepage_version": 1,
                "role": current_user.role.name,
            },
        )