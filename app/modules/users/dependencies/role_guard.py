from fastapi import Depends, HTTPException, status

from app.modules.users.dependencies.current_user import (
    get_current_user,
)

from app.modules.users.models.user_model import (
    UserModel,
)


def require_roles(*allowed_roles: str):

    def role_checker(
        current_user: UserModel = Depends(
            get_current_user
        )
    ) -> UserModel:

        user_role = current_user.role.name

        if user_role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Access denied"
            )

        return current_user

    return role_checker