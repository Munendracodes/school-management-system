from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
    Query,
    status
)

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.modules.users.schemas.user_schema import (
    CreateUserRequest,
    UpdateUserRequest,
    UserResponse,
    UserListResponse
)

from app.modules.users.services.user_service import (
    UserService
)

from app.modules.users.dependencies.current_user import (
    get_current_user,
)

from app.modules.users.dependencies.role_guard import (
    require_roles
)

from app.modules.users.constants.role_constants import (
    Role
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post(
    "",
    status_code=status.HTTP_201_CREATED
)
def create_user(
    payload: CreateUserRequest,
    db: Session = Depends(get_db),
    current_user = Depends(
        require_roles(
            Role.SUPER_ADMIN,
            Role.ADMIN
        )
    )
):

    return UserService.create_user(
        db=db,
        payload=payload,
        created_by=current_user.id
    )


@router.get(
    "",
    response_model=UserListResponse
)
def get_users(
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
    search: str | None = Query(None),
    role_id: UUID | None = Query(None),
    is_active: bool | None = Query(None),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return UserService.get_users(
        db=db,
        page=page,
        size=size,
        search=search,
        role_id=role_id,
        is_active=is_active
    )


@router.get(
    "/{user_id}",
    response_model=UserResponse
)
def get_user_by_id(
    user_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return UserService.get_user_by_id(
        db=db,
        user_id=user_id
    )


@router.put(
    "/{user_id}",
    response_model=UserResponse
)
def update_user(
    user_id: UUID,
    payload: UpdateUserRequest,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles(
            Role.SUPER_ADMIN,
            Role.ADMIN
        )
    )
):

    return UserService.update_user(
        db=db,
        user_id=user_id,
        payload=payload
    )


@router.delete(
    "/{user_id}"
)
def delete_user(
    user_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles(
            Role.SUPER_ADMIN,
            Role.ADMIN
        )
    )
):

    return UserService.delete_user(
        db=db,
        user_id=user_id
    )