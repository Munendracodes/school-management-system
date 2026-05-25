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
                    "icon_color": "#2457FF",
                    "background_color": "#F5F7FF",

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
                    "icon_color": "#FF4DA6",
                    "background_color": "#FFF1F7",

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
                    "icon_color": "#FF8A00",
                    "background_color": "#FFF8F1",

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
                    "icon_color": "#7C4DFF",
                    "background_color": "#F8F5FF",

                    "redirect_url": (
                        "/timetables"
                    ),

                    "background_color": "#FFF7ED",
                },
            ],
        }