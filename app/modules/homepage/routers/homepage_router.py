from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
)

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.modules.homepage.schemas.homepage_schema import (
    HomepageWidgetCreateSchema,
    HomepageWidgetUpdateSchema,
    HomepageWidgetResponseSchema,
)

from app.modules.homepage.services.homepage_service import (
    HomepageService,
)

from app.modules.users.dependencies.current_user import (
    get_current_user,
)

router = APIRouter(
    prefix="/homepage",
    tags=["Homepage"],
)


@router.post(
    "/widgets",
    response_model=HomepageWidgetResponseSchema,
)
def create_widget(
    payload: HomepageWidgetCreateSchema,
    db: Session = Depends(get_db),
):
    return HomepageService.create_widget(
        db,
        payload,
    )


@router.get("")
def get_homepage(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    return HomepageService.get_dynamic_homepage(
        db,
        current_user,
    )


@router.get(
    "/widgets",
    response_model=list[HomepageWidgetResponseSchema],
)
def get_all_widgets(
    db: Session = Depends(get_db),
):
    return HomepageService.get_all_widgets(
        db,
    )


@router.put(
    "/widgets/{widget_id}",
    response_model=HomepageWidgetResponseSchema,
)
def update_widget(
    widget_id: UUID,
    payload: HomepageWidgetUpdateSchema,
    db: Session = Depends(get_db),
):
    return HomepageService.update_widget(
        db,
        widget_id,
        payload,
    )


@router.delete(
    "/widgets/{widget_id}",
)
def delete_widget(
    widget_id: UUID,
    db: Session = Depends(get_db),
):
    return HomepageService.delete_widget(
        db,
        widget_id,
    )