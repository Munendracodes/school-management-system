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
          "icon_color": "#2457FF",
          "background_color": "#F5F7FF",

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
          "icon_color": "#FF4DA6",
          "background_color": "#FFF1F7",

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
          "icon_color": "#FF8A00",
          "background_color": "#FFF8F1",

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
          "icon_color": "#7C4DFF",
          "background_color": "#F8F5FF",

                    "redirect_url": (
                        "/progress-reports"
                    ),

                    "background_color": "#FFF7ED",
                },
            ],
        }