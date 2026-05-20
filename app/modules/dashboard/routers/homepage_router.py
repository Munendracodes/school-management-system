from fastapi import APIRouter, Depends

from app.modules.users.dependencies.current_user import (
    get_current_user,
)

from app.modules.users.models.user_model import (
    UserModel,
)


router = APIRouter(
    prefix="/homepage",
    tags=["Homepage"]
)


@router.get("")
def get_homepage(
    current_user: UserModel = Depends(
        get_current_user
    )
):

    role = current_user.role.name

    modules = []

    if role == "SUPER_ADMIN":

        modules = [
            {
                "key": "dashboard",
                "name": "Dashboard",
                "icon": "layout-dashboard"
            },
            {
                "key": "schools",
                "name": "Schools",
                "icon": "building"
            },
            {
                "key": "users",
                "name": "Users",
                "icon": "users"
            },
            {
                "key": "roles",
                "name": "Roles",
                "icon": "shield"
            }
        ]

    elif role == "ADMIN":

        modules = [
            {
                "key": "dashboard",
                "name": "Dashboard",
                "icon": "layout-dashboard"
            },
            {
                "key": "students",
                "name": "Students",
                "icon": "graduation-cap"
            },
            {
                "key": "teachers",
                "name": "Teachers",
                "icon": "briefcase"
            },
            {
                "key": "attendance",
                "name": "Attendance",
                "icon": "calendar-check"
            }
        ]

    elif role == "TEACHER":

        modules = [
            {
                "key": "attendance",
                "name": "Attendance",
                "icon": "calendar-check"
            },
            {
                "key": "students",
                "name": "Students",
                "icon": "graduation-cap"
            },
            {
                "key": "marks",
                "name": "Marks",
                "icon": "clipboard-list"
            }
        ]

    elif role == "STUDENT":

        modules = [
            {
                "key": "profile",
                "name": "Profile",
                "icon": "user"
            },
            {
                "key": "attendance",
                "name": "Attendance",
                "icon": "calendar-check"
            },
            {
                "key": "marks",
                "name": "Marks",
                "icon": "clipboard-list"
            }
        ]

    elif role == "PARENT":

        modules = [
            {
                "key": "children",
                "name": "Children",
                "icon": "users"
            },
            {
                "key": "attendance",
                "name": "Attendance",
                "icon": "calendar-check"
            },
            {
                "key": "fees",
                "name": "Fees",
                "icon": "credit-card"
            }
        ]

    return {
        "user": {
            "id": str(current_user.id),
            "full_name": current_user.full_name,
            "role": role
        },

        "modules": modules,

        "stats": {
            "students_count": 1200,
            "teachers_count": 85,
            "today_attendance": 92
        },

        "quick_actions": [
            "Add Student",
            "Create Teacher",
            "Take Attendance"
        ]
    }