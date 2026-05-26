from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.modules.settings.schemas import (
    BootstrapResponse,
    SchoolSettingsCreate,
    SchoolSettingsResponse,
    SchoolSettingsUpdate,
)

from app.modules.settings.service import (
    SchoolSettingsService,
)

router = APIRouter(
    prefix="/settings",
    tags=["🎨 Homepage CMS"]
)


@router.get(
    "/",
    response_model=SchoolSettingsResponse,
)
def get_settings(
    db: Session = Depends(get_db),
):
    settings = (
        SchoolSettingsService
        .get_settings(db)
    )

    if not settings:
        raise HTTPException(
            status_code=404,
            detail="Settings not found",
        )

    return settings


@router.post(
    "/",
    response_model=SchoolSettingsResponse,
)
def create_settings(
    payload: SchoolSettingsCreate,
    db: Session = Depends(get_db),
):
    try:
        return (
            SchoolSettingsService
            .create_settings(
                db,
                payload,
            )
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.put(
    "/",
    response_model=SchoolSettingsResponse,
)
def update_settings(
    payload: SchoolSettingsUpdate,
    db: Session = Depends(get_db),
):
    try:
        return (
            SchoolSettingsService
            .update_settings(
                db,
                payload,
            )
        )

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )
    
@router.delete(
"/",
)
def delete_settings(
    db: Session = Depends(get_db),
):
    try:
        SchoolSettingsService.delete_settings(
            db
        )

        return {
            "success": True,
            "message":
                "School settings deleted successfully"
        }

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )

@router.get(
    "/bootstrap",
    response_model=BootstrapResponse,
)
def get_bootstrap(
    db: Session = Depends(get_db),
):
    try:
        return (
            SchoolSettingsService
            .get_bootstrap_data(db)
        )

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )