import uuid
from fastapi import APIRouter, Depends, status, Request

from homepp.core.common.types.auth import SessionId
from homepp.core.common.mediator import Mediator
from homepp.core.user.handlers.logout import LogoutUserCommand
from ...deps.mediator import provide_mediator_stub


router = APIRouter()


@router.post(
    "/logout",
    status_code=status.HTTP_200_OK,
)
async def logout(
    request: Request,
    mediator: Mediator = Depends(provide_mediator_stub),
):
    session_id = SessionId(uuid.UUID(request.cookies["session_id"]))
    await mediator.send(LogoutUserCommand(session_id=session_id))
