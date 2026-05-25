from fastapi import (
    APIRouter,
    Depends,
)

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.modules.homepage.services.homepage_service import (
    HomepageService,
)

from app.modules.users.dependencies.current_user import (
    get_current_user,
)

router = APIRouter(
    prefix="/homepage",
    tags=["Homepage"],
)


@router.get("")
def get_homepage(
    db: Session = Depends(get_db),
    current_user=Depends(
        get_current_user,
    ),
):
    return HomepageService.get_homepage(
        db,
        current_user,
    )