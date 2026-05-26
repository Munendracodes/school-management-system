from fastapi import (
    APIRouter,
    Depends,
)

from sqlalchemy.orm import Session

from app.database.session import (
    get_db,
)

from app.modules.teacher_section_map.schemas.teacher_section_map_schema import (
    TeacherSectionMapCreateSchema,
    TeacherSectionMapResponseSchema,
)

from app.modules.teacher_section_map.services.teacher_section_map_service import (
    TeacherSectionMapService,
)

router = APIRouter(
    prefix="/teacher-section-mappings",
    tags=["🔗 Mapping Engine"]
)


@router.post(
    "",
    response_model=TeacherSectionMapResponseSchema,
)
def create_mapping(
    payload:
    TeacherSectionMapCreateSchema,
    db: Session = Depends(
        get_db
    ),
):

    return (
        TeacherSectionMapService.create_mapping(
            db,
            payload,
        )
    )


@router.get("")
def get_mappings(
    db: Session = Depends(
        get_db
    ),
):

    return (
        TeacherSectionMapService.get_mappings(
            db
        )
    )