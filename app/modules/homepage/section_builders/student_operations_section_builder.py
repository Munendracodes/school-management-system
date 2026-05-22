class StudentOperationsSectionBuilder:

    @staticmethod
    def build():

        return {

            "section_type": "MODULE_GRID",

            "title": "Student Operations",

            "description": (
                "Manage students, attendance, "
                "exams and reports"
            ),

            "display_order": 4,

            "items": [

                {
                    "module_type": "GRID_ITEM",

                    "title": "Students",

                    "description": (
                        "Manage student information"
                    ),

                    "icon": "students",

                    "redirect_url": (
                        "/students"
                    ),

                    "background_color": "#F0FDF4",
                },

                {
                    "module_type": "GRID_ITEM",

                    "title": "Attendance",

                    "description": (
                        "Mark and manage attendance"
                    ),

                    "icon": "attendance",

                    "redirect_url": (
                        "/attendance"
                    ),

                    "background_color": "#EFF6FF",
                },

                {
                    "module_type": "GRID_ITEM",

                    "title": "Examinations",

                    "description": (
                        "Manage exams and schedules"
                    ),

                    "icon": "examinations",

                    "redirect_url": (
                        "/examinations"
                    ),

                    "background_color": "#FAF5FF",
                },

                {
                    "module_type": "GRID_ITEM",

                    "title": "Progress Reports",

                    "description": (
                        "Create and manage "
                        "progress reports"
                    ),

                    "icon": "reports",

                    "redirect_url": (
                        "/progress-reports"
                    ),

                    "background_color": "#FFF7ED",
                },
            ],
        }