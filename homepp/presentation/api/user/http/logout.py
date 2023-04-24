import uuid
from fastapi import APIRouter, Depends, status, Cookie

from homepp.core.common.types.auth import SessionId
from homepp.core.common.exc.auth import SessionNotFoundException
from homepp.core.common.mediator import Mediator
from homepp.core.user.handlers.logout import LogoutUserCommand
from ...deps.mediator import provide_mediator_stub


router = APIRouter()


@router.post(
    "/logout",
    status_code=status.HTTP_200_OK,
)
async def logout(
    mediator: Mediator = Depends(provide_mediator_stub),
    session_id: str | None = Cookie(default=None),
):
    if not session_id:
        raise SessionNotFoundException
    await mediator.send(
        LogoutUserCommand(session_id=SessionId(uuid.UUID(session_id)))
    )
