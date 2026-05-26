from uuid import UUID

from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.modules.users.schemas.role_schema import (
    RoleListResponse,
    RoleResponse
)

from app.modules.users.services.role_service import (
    RoleService
)

from app.modules.users.dependencies.current_user import (
    get_current_user,
)

router = APIRouter(
    prefix="/roles",
    tags=["👤 User Management"]
)


@router.get(
    "",
    response_model=RoleListResponse
)
def get_roles(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return RoleService.get_roles(
        db
    )


@router.get(
    "/{role_id}",
    response_model=RoleResponse
)
def get_role_by_id(
    role_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return RoleService.get_role_by_id(
        db,
        role_id
    )