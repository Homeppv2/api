from fastapi import APIRouter, Depends, status

from homepp.core.user.domain.models import User
from .models.response import UserResponse
from ...deps.auth import get_current_user


router = APIRouter()


@router.post(
    "/me",
    status_code=status.HTTP_200_OK,
)
async def get_current(
    user: User = Depends(get_current_user),
) -> UserResponse:
    return UserResponse(username=user.username.value, email=user.email.value)  # type: ignore # noqa
