from fastapi import (
    HTTPException,
    status,
)

from app.modules.homepage.repositories.homepage_repository import (
    HomepageRepository,
)

from app.modules.homepage.assemblers.homepage_assembler import (
    HomepageAssembler,
)

class HomepageService:

    @staticmethod
    def create_widget(
        db,
        payload,
    ):
        return HomepageRepository.create(
            db,
            payload.model_dump(),
        )

    @staticmethod
    def get_homepage(
        db,
        role: str,
    ):
        return HomepageRepository.get_visible_widgets(
            db,
            role,
        )

    @staticmethod
    def get_all_widgets(
        db,
    ):
        return HomepageRepository.get_all(db)

    @staticmethod
    def update_widget(
        db,
        widget_id,
        payload,
    ):
        widget = HomepageRepository.get_by_id(
            db,
            widget_id,
        )

        if not widget:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Widget not found",
            )

        return HomepageRepository.update(
            db,
            widget,
            payload.model_dump(exclude_unset=True),
        )

    @staticmethod
    def delete_widget(
        db,
        widget_id,
    ):
        widget = HomepageRepository.get_by_id(
            db,
            widget_id,
        )

        if not widget:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Widget not found",
            )

        HomepageRepository.soft_delete(
            db,
            widget,
        )

        return {
            "message": "Widget deleted successfully",
        }
    
    @staticmethod
    def get_dynamic_homepage(
        db,
        current_user,
    ):
        return HomepageAssembler.build(
            db,
            current_user,
        )