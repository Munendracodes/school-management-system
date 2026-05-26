from datetime import datetime
from zoneinfo import ZoneInfo

from sqlalchemy.orm import Session

from app.modules.homepage.repositories.homepage_section_repository import (
    HomepageSectionRepository,
)

from app.modules.homepage.repositories.homepage_item_repository import (
    HomepageItemRepository,
)

from app.modules.student.repositories.student_repository import (
    StudentRepository,
)

from app.modules.teacher.repositories.teacher_repository import (
    TeacherRepository,
)

from app.modules.parent.repositories.parent_repository import (
    ParentRepository)


class HomepageService:

    @staticmethod
    def get_dynamic_value(
        db,
        data_source,
    ):

        mapping = {

            "TOTAL_STUDENTS":
            lambda: StudentRepository.get_count(
                db
            ),

            "TOTAL_TEACHERS":
            lambda: TeacherRepository.get_count(
                db
            ),

            "TOTAL_PARENTS":
            lambda: ParentRepository.get_count(
                db
            ),

        }

        value_fn = mapping.get(
            data_source
        )

        return (
            value_fn()
            if value_fn
            else None
        )


    @staticmethod
    def build_item(
        db,
        item,
    ):

        config = (
            item.config_json
            or {}
        )

        item_data = {

            "type":
            item.item_type,

            "title":
            item.title,

            "redirect_url":
            item.redirect_url,
        }

        if item.icon:

            item_data[
                "icon"
            ] = item.icon


        item_type = item.item_type


        if item_type == "METRIC_CARD":

            value = (
                HomepageService
                .get_dynamic_value(
                    db,
                    config.get(
                        "data_source"
                    )
                )
            )

            item_data.update({

                "value":
                value,

                "icon_color":
                config.get(
                    "icon_color"
                ),

                "background_color":
                config.get(
                    "background_color"
                )

            })


        elif item_type == "ACTION_CARD":

            item_data.update({

                "icon_color":
                config.get(
                    "icon_color"
                ),

                "background_color":
                config.get(
                    "background_color"
                )
            })


        elif item_type == "BANNER_CARD":

            item_data.update({

                "subtitle":
                config.get(
                    "subtitle"
                ),

                "media_type":
                config.get(
                    "media_type"
                ),

                "media_url":
                config.get(
                    "media_url"
                ),

                "cta_text":
                config.get(
                    "cta_text"
                ),

                "background_color":
                config.get(
                    "background_color"
                ),

                "text_color":
                config.get(
                    "text_color"
                )
            })


        elif item_type == "NOTICE_CARD":

            item_data.update({

                "description":
                config.get(
                    "description"
                ),

                "date":
                config.get(
                    "date"
                )

            })

        return item_data


    @staticmethod
    def get_hero_banner(
        user_name,
    ):

        indian_now = datetime.now(
            ZoneInfo(
                "Asia/Kolkata"
            )
        )

        current_hour = (
            indian_now.hour
        )

        if current_hour < 12:

            greeting = (
                "Good Morning"
            )

        elif current_hour < 17:

            greeting = (
                "Good Afternoon"
            )

        else:

            greeting = (
                "Good Evening"
            )

        return {

            "title":
            f"{greeting}, {user_name} 👋",

            "subtitle":
            indian_now.strftime(
                "%A, %d %B %Y"
            ),

            "image_url":
            ""
        }


    @staticmethod
    def get_homepage(
        db: Session,
        current_user,
    ):

        role = (
            current_user
            .role
            .name
        )

        sections = (
            HomepageSectionRepository
            .get_visible_sections(
                db,
                role
            )
        )

        final_sections=[]

        for section in sections:

            section_data = {

                "type":
                section.section_type,

                "title":
                section.title,

                "background_color":
                section.background_color,

                "text_color":
                section.text_color,

                "display_order":
                section.display_order,

                "items":[]
            }

            items=(
                HomepageItemRepository
                .get_items(
                    db,
                    section.id,
                    role
                )
            )

            for item in items:

                section_data[
                    "items"
                ].append(

                    HomepageService
                    .build_item(
                        db,
                        item
                    )
                )

            final_sections.append(
                section_data
            )

        return {

            "user":{

                "full_name":
                current_user.full_name,

                "role":
                role
            },

            "header":{

                "school_name":
                "Sunshine Public School",

                "school_logo":
                "",

                "screen_title":
                "Admin Dashboard",

                "notification_count":
                4
            },

            "hero_banner":
            HomepageService
            .get_hero_banner(
                current_user.full_name
            ),

            "sections":
            final_sections
        }