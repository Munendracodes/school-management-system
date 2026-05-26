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

from app.modules.users.dependencies.current_user import (
    get_current_user,
)

from app.modules.users.models.user_model import (
    UserModel,
)


router = APIRouter(
    prefix="/homepage-items",
    tags=["🎨 Homepage CMS"]
)


@router.post(
    "",
    response_model=HomepageItemResponseSchema,
)
def create_item(
    payload: HomepageItemCreateSchema,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
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
    current_user: UserModel = Depends(get_current_user),
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
    current_user: UserModel = Depends(get_current_user),
):

    return HomepageItemService.update(
        db,
        item_id,
        payload,
    )


@router.delete(
    "/{item_id}",
    response_model=HomepageItemResponseSchema,
)
def delete_item(
    item_id: UUID,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):

    return HomepageItemService.delete(
        db,
        item_id,
    )