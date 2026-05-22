from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
)

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.modules.section.schemas.section_schema import (
    SectionCreateSchema,
    SectionUpdateSchema,
    SectionResponseSchema,
)

from app.modules.section.services.section_service import (
    SectionService,
)

router = APIRouter(
    prefix="/sections",
    tags=["Sections"],
)


@router.post(
    "",
    response_model=SectionResponseSchema,
)
def create_section(
    payload: SectionCreateSchema,
    db: Session = Depends(get_db),
):
    return SectionService.create_section(
        db,
        payload,
    )


@router.get(
    "",
    response_model=list[SectionResponseSchema],
)
def get_sections(
    db: Session = Depends(get_db),
):
    return SectionService.get_sections(db)


@router.get(
    "/{section_id}",
    response_model=SectionResponseSchema,
)
def get_section_by_id(
    section_id: UUID,
    db: Session = Depends(get_db),
):
    return SectionService.get_section_by_id(
        db,
        section_id,
    )


@router.put(
    "/{section_id}",
    response_model=SectionResponseSchema,
)
def update_section(
    section_id: UUID,
    payload: SectionUpdateSchema,
    db: Session = Depends(get_db),
):
    return SectionService.update_section(
        db,
        section_id,
        payload,
    )


@router.delete("/{section_id}")
def delete_section(
    section_id: UUID,
    db: Session = Depends(get_db),
):
    return SectionService.delete_section(
        db,
        section_id,
    )