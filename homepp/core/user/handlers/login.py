import uuid
from dataclasses import dataclass

from homepp.core.common.handler import Handler
from homepp.core.common.uow import UnitOfWork
from homepp.core.common.types.user import RawPassword, Email
from homepp.core.user.protocols.user_gateway import UserReadGateway
from homepp.core.user.protocols.token_gateway import TokenGateway
from homepp.core.user.domain.services.auth import AuthUserService
from homepp.core.common.exc.auth import InvalidCredentialsException


@dataclass
class LoginUserCommand:
    email: str
    raw_password: str


class LoginUserHandler(Handler[LoginUserCommand, uuid.UUID]):
    def __init__(
        self,
        auth_service: AuthUserService,
        user_read_gateway: UserReadGateway,
        token_gateway: TokenGateway,
        uow: UnitOfWork,
    ):
        self._auth_service = auth_service
        self._user_read_gateway = user_read_gateway
        self._token_gateway = token_gateway
        self._uow = uow

    async def execute(self, command: LoginUserCommand) -> uuid.UUID:
        user = await self._user_read_gateway.get_user_by_email(
            Email(command.email)
        )
        if not user:
            raise InvalidCredentialsException

        verify = self._auth_service.verify_pass(
            RawPassword(command.raw_password), user.hashed_password
        )

        if not verify:
            raise InvalidCredentialsException

        session_id = self._auth_service.generate_session_id()
        token = self._auth_service.create_token(user.id)  # type: ignore
        await self._token_gateway.create(session_id, token)
        return session_id
