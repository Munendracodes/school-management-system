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
                },

                {
                    "title": "Mark Attendance",

                    "icon": "attendance",

                    "redirect_url": (
                        "/attendance"
                    ),
                },
            ],
        }