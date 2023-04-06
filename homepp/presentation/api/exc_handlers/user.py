from fastapi import FastAPI, Request, status
from fastapi.responses import ORJSONResponse

from homepp.core.common.exc.base import ValidationError
from homepp.core.common.exc.user import (
    UserDoesNotExistsException,
    UserAlreadyExistsException,
)
from .utils import make_detail


async def user_does_not_exist_handler(
    request: Request, exc: UserDoesNotExistsException
) -> ORJSONResponse:
    return ORJSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content=make_detail("User does not exist"),
    )


async def user_already_exists_handler(
    request: Request, exc: UserAlreadyExistsException
) -> ORJSONResponse:
    return ORJSONResponse(
        status_code=status.HTTP_403_FORBIDDEN,
        content=make_detail("User already exists"),
    )


async def validation_error_handler(
    request: Request, exc: ValidationError
) -> ORJSONResponse:
    return ORJSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=make_detail(exc.message),
    )


def setup_user_exc_handlers(app: FastAPI) -> None:
    app.add_exception_handler(
        UserDoesNotExistsException, user_does_not_exist_handler
    )
    app.add_exception_handler(
        UserAlreadyExistsException, user_does_not_exist_handler
    )
    app.add_exception_handler(ValidationError, validation_error_handler)
