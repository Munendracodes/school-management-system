from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
)

from sqlalchemy.orm import Session

from app.database.session import (
    get_db,
)

from app.modules.homepage.schemas.homepage_item_schema import (
    HomepageItemCreateSchema,
    HomepageItemUpdateSchema,
    HomepageItemResponseSchema,
)

from app.modules.homepage.services.homepage_item_service import (
    HomepageItemService,
)


router = APIRouter(
    prefix="/homepage/items",
    tags=["Homepage Items"],
)


@router.post(
    "",
    response_model=HomepageItemResponseSchema,
)
def create_item(
    payload: HomepageItemCreateSchema,
    db: Session = Depends(get_db),
):

    return HomepageItemService.create(
        db,
        payload,
    )


@router.get(
    "",
    response_model=list[
        HomepageItemResponseSchema
    ],
)
def get_items(
    db: Session = Depends(get_db),
):

    return HomepageItemService.get_all(
        db,
    )


@router.put(
    "/{item_id}",
    response_model=HomepageItemResponseSchema,
)
def update_item(
    item_id: UUID,
    payload: HomepageItemUpdateSchema,
    db: Session = Depends(get_db),
):

    return HomepageItemService.update(
        db,
        item_id,
        payload,
    )


@router.delete(
    "/{item_id}",
)
def delete_item(
    item_id: UUID,
    db: Session = Depends(get_db),
):

    return HomepageItemService.delete(
        db,
        item_id,
    )