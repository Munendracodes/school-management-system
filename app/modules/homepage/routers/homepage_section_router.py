from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
)

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.modules.homepage.schemas.homepage_section_schema import (
    HomepageSectionCreateSchema,
    HomepageSectionUpdateSchema,
    HomepageSectionResponseSchema,
)

from app.modules.homepage.services.homepage_section_service import (
    HomepageSectionService,
)

from app.modules.users.dependencies.current_user import (
    get_current_user,
)

from app.modules.users.models.user_model import (
    UserModel,
)

router = APIRouter(
    prefix="/homepage-sections",
    tags=["🎨 Homepage CMS"]
)


@router.post(
    "",
    response_model=HomepageSectionResponseSchema,
)
def create_section(
    payload: HomepageSectionCreateSchema,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    return HomepageSectionService.create(
        db,
        payload,
    )


@router.get(
    "",
    response_model=list[
        HomepageSectionResponseSchema
    ],
)
def get_sections(
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    return HomepageSectionService.get_all(
        db,
    )


@router.put(
    "/{section_id}",
    response_model=HomepageSectionResponseSchema,
)
def update_section(
    section_id: UUID,
    payload: HomepageSectionUpdateSchema,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    return HomepageSectionService.update(
        db,
        section_id,
        payload,
    )


@router.delete(
    "/{section_id}",
    response_model=HomepageSectionResponseSchema,
)
def delete_section(
    section_id: UUID,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    return HomepageSectionService.delete(
        db,
        section_id,
    )