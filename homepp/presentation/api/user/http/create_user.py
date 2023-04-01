from fastapi import APIRouter, Depends, status

from homepp.core.common.mediator import Mediator
from homepp.core.user.handlers.create_user import CreateUserCommand
from .models.request import UserSignUpRequest
from ...deps.mediator import provide_mediator_stub


router = APIRouter()


@router.post(
    "/create",
    status_code=status.HTTP_201_CREATED,
)
async def create_user(
    new_user: UserSignUpRequest,
    mediator: Mediator = Depends(provide_mediator_stub),
):
    await mediator.send(
        CreateUserCommand(
            username=new_user.username,
            raw_password=new_user.password,
            email=new_user.email,
        )
    )

    return {"message": "User created successfully"}
