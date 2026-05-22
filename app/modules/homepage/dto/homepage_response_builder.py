from typing import Any


class HomepageResponseBuilder:

    @staticmethod
    def build(
        *,
        user: dict,
        header: dict,
        hero_banner: dict,
        sections: list,
        bottom_navigation: list,
        meta: dict,
    ) -> dict[str, Any]:

        return {
            "user": user,
            "header": header,
            "hero_banner": hero_banner,
            "sections": sections,
            "bottom_navigation": bottom_navigation,
            "meta": meta,
        }