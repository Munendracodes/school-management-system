class OverviewSectionBuilder:

    @staticmethod
    def build(
        dashboard,
    ):

        return {

            "section_type": "OVERVIEW_CARDS",

            "title": "Today's Overview",

            "display_order": 1,

            "items": [

                {
                    "card_type": "METRIC_CARD",

                    "title": "Total Students",

                    "value": dashboard.get(
                        "total_students",
                        0,
                    ),

                    "icon": "students",
                    "icon_color": "#2457FF",
                    "background_color": "#F5F7FF"
                },

                {
                    "card_type": "METRIC_CARD",

                    "title": "Total Teachers",

                    "value": dashboard.get(
                        "total_teachers",
                        0,
                    ),

                    "icon": "teachers",
                    "icon_color": "#FF4DA6",
                    "background_color": "#FFF1F7"
                },
            ],
        }