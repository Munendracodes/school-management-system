class QuickActionsSectionBuilder:

    @staticmethod
    def build():

        return {

            "section_type": "QUICK_ACTIONS",

            "title": "Quick Actions",

            "display_order": 2,

            "items": [

                {
                    "title": "Add Student",

                    "icon": "student_add",

                    "redirect_url": (
                        "/students/create"
                    ),
                    "icon_color": "#2457FF",
                    "background_color": "#F5F7FF",
                },

                {
                    "title": "Mark Attendance",

                    "icon": "attendance",

                    "redirect_url": (
                        "/attendance"
                    ),
                    "icon_color": "#FF4DA6",
                    "background_color": "#FFF1F7",  
                },
            ],
        }