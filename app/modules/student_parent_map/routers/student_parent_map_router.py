from fastapi import (
    APIRouter,
    Depends,
)

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.modules.student_parent_map.schemas.student_parent_map_schema import (
    StudentParentMapCreateSchema,
    StudentParentMapResponseSchema,
)

from app.modules.student_parent_map.services.student_parent_map_service import (
    StudentParentMapService,
)

from app.modules.users.dependencies.current_user import (
    get_current_user,
)

from app.modules.users.models.user_model import (
    UserModel,
)

router = APIRouter(
    prefix="/student-parent-mappings",
    tags=["🔗 Mapping Engine"]
)


@router.post(
    "",
    response_model=StudentParentMapResponseSchema,
)
def create_mapping(
    payload: StudentParentMapCreateSchema,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):

    return StudentParentMapService.create_mapping(
        db,
        payload,
    )