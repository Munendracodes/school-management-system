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

router = APIRouter(
    prefix="/student-parent-mappings",
    tags=["Student Parent Mapping"],
)


@router.post(
    "",
    response_model=StudentParentMapResponseSchema,
)
def create_mapping(
    payload: StudentParentMapCreateSchema,
    db: Session = Depends(get_db),
):

    return StudentParentMapService.create_mapping(
        db,
        payload,
    )