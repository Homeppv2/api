from homepp.core.user.protocols.token_gateway import TokenGateway
from homepp.core.user.protocols.user_gateway import (
    UserWriteGateway,
    UserReadGateway,
)
from .mediator import MediatorImpl, Mediator

from homepp.core.user.domain.services.user import UserService
from homepp.core.user.domain.services.auth import AuthUserService
from homepp.core.common.uow import UnitOfWork
from homepp.core.user.handlers.create_user import (
    CreateUserCommand,
    CreateUserHandler,
)
from homepp.core.user.handlers.current_user import (
    GetCurrentUserCommand,
    GetCurrentUserHandler,
)
from homepp.core.user.handlers.login import (
    LoginUserCommand,
    LoginUserHandler,
)
from homepp.core.user.handlers.logout import (
    LogoutUserCommand,
    LogoutUserHandler,
)
from homepp.core.user.handlers.get_user_by_hw_key import (
    GetUserByHwKeyCommand,
    GetUserByHwKeyHandler,
)


def build_mediator(
    user_write_gateway: UserWriteGateway,
    user_read_gateway: UserReadGateway,
    uow: UnitOfWork,
    token_gateway: TokenGateway,
    secret_key: str,
    token_expiration: int,
) -> Mediator:
    mediator = MediatorImpl()
    user_service = UserService()
    auth_service = AuthUserService(secret_key, token_expiration)

    mediator.bind(
        CreateUserCommand,
        CreateUserHandler(user_service, auth_service, user_write_gateway, uow),
    )
    mediator.bind(
        GetCurrentUserCommand,
        GetCurrentUserHandler(
            auth_service, user_read_gateway, token_gateway, uow
        ),
    )
    mediator.bind(
        LoginUserCommand,
        LoginUserHandler(auth_service, user_read_gateway, token_gateway, uow),
    )
    mediator.bind(
        LogoutUserCommand,
        LogoutUserHandler(auth_service, user_read_gateway, token_gateway),
    )
    mediator.bind(
        GetUserByHwKeyCommand, GetUserByHwKeyHandler(user_read_gateway)
    )

    return mediator
