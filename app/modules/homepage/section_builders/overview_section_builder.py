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

                    "color": "#2563EB",
                },

                {
                    "card_type": "METRIC_CARD",

                    "title": "Total Teachers",

                    "value": dashboard.get(
                        "total_teachers",
                        0,
                    ),

                    "icon": "teachers",

                    "color": "#16A34A",
                },
            ],
        }