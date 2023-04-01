from fastapi import FastAPI, Request, status
from fastapi.responses import ORJSONResponse

from homepp.core.common.exc.auth import (
    InvalidTokenException,
    InvalidCredentialsException,
    SessionNotFoundException,
)


def make_detail(message: str):
    return {"detail": message}


async def invalid_token_exc_handler(
    request: Request, exc: InvalidTokenException
):
    return ORJSONResponse(
        status_code=status.HTTP_403_FORBIDDEN,
        content=make_detail("Invalid token"),
    )


async def invalid_credentials_exc_handler(
    request: Request, exc: InvalidCredentialsException
):
    return ORJSONResponse(
        status_code=status.HTTP_403_FORBIDDEN,
        content=make_detail("Invalid credentials"),
    )


async def session_not_found_exc_handler(
    request: Request, exc: SessionNotFoundException
):
    return ORJSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content=make_detail("Unauthorized"),
    )


def setup_auth_exc_handlers(app: FastAPI):
    app.add_exception_handler(InvalidTokenException, invalid_token_exc_handler)
    app.add_exception_handler(
        InvalidCredentialsException, invalid_credentials_exc_handler
    )
    app.add_exception_handler(
        SessionNotFoundException, session_not_found_exc_handler
    )
