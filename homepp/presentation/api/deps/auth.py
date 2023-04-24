from uuid import UUID
from fastapi import Depends, Cookie
from fastapi.security import OAuth2PasswordRequestForm

from homepp.core.user.domain.models import User
from homepp.core.common.types.user import RawPassword
from homepp.core.common.types.auth import SessionId
from homepp.core.user.handlers.current_user import GetCurrentUserCommand
from homepp.core.common.mediator import Mediator
from homepp.core.common.exc.auth import SessionNotFoundException
from ..user.http.models.request import UserLoginFormRequest
from .mediator import provide_mediator_stub


def get_login_form(
    user: OAuth2PasswordRequestForm = Depends(),
) -> UserLoginFormRequest:
    return UserLoginFormRequest(
        username=user.username,
        password=RawPassword(user.password),
    )


async def current_user(
    mediator: Mediator = Depends(provide_mediator_stub),
    session_id: str | None = Cookie(default=None),
) -> User:
    if not session_id:
        raise SessionNotFoundException

    user = await mediator.send(
        GetCurrentUserCommand(SessionId(UUID(session_id)))
    )
    if not user:
        raise SessionNotFoundException
    return user
