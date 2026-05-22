class AcademicStructureSectionBuilder:

    @staticmethod
    def build():

        return {

            "section_type": "MODULE_GRID",

            "title": "Academic Structure",

            "description": (
                "Manage classes, sections, "
                "subjects and schedules"
            ),

            "display_order": 3,

            "items": [

                {
                    "module_type": "GRID_ITEM",

                    "title": "Classes",

                    "description": (
                        "Manage all classes"
                    ),

                    "icon": "classroom",

                    "redirect_url": (
                        "/classrooms"
                    ),

                    "background_color": "#EFF6FF",
                },

                {
                    "module_type": "GRID_ITEM",

                    "title": "Sections",

                    "description": (
                        "Manage sections / divisions"
                    ),

                    "icon": "sections",

                    "redirect_url": (
                        "/sections"
                    ),

                    "background_color": "#F0FDF4",
                },

                {
                    "module_type": "GRID_ITEM",

                    "title": "Subjects",

                    "description": (
                        "Manage all subjects"
                    ),

                    "icon": "subjects",

                    "redirect_url": (
                        "/subjects"
                    ),

                    "background_color": "#FAF5FF",
                },

                {
                    "module_type": "GRID_ITEM",

                    "title": "Timetables",

                    "description": (
                        "Manage schedules "
                        "and timetables"
                    ),

                    "icon": "timetable",

                    "redirect_url": (
                        "/timetables"
                    ),

                    "background_color": "#FFF7ED",
                },
            ],
        }