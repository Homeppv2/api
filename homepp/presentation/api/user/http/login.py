from fastapi import APIRouter, Depends, status, Response

from homepp.core.common.mediator import Mediator
from homepp.core.user.handlers.login import LoginUserCommand
from .models.request import UserLoginFormRequest
from ...deps.mediator import provide_mediator_stub
from ...deps.auth import get_login_form


router = APIRouter()


@router.post(
    "/login",
    status_code=status.HTTP_200_OK,
)
async def login(
    response: Response,
    form_data: UserLoginFormRequest = Depends(get_login_form),
    mediator: Mediator = Depends(provide_mediator_stub),
):
    session_id = await mediator.send(
        LoginUserCommand(
            raw_password=form_data.password,
            email=form_data.username,
        )
    )
    response.set_cookie(key="session_id", value=session_id)
    return session_id
