from dataclasses import dataclass

from homepp.core.common.handler import Handler
from homepp.core.common.types.auth import SessionId
from homepp.core.user.protocols.user_gateway import UserReadGateway
from homepp.core.user.protocols.token_gateway import TokenGateway
from homepp.core.user.domain.services.auth import AuthUserService
from homepp.core.common.exc.auth import SessionNotFoundException


@dataclass
class LogoutUserCommand:
    session_id: SessionId


class LogoutUserHandler(Handler[LogoutUserCommand, None]):
    def __init__(
        self,
        auth_service: AuthUserService,
        user_read_gateway: UserReadGateway,
        token_gateway: TokenGateway,
    ):
        self._auth_service = auth_service
        self._user_read_gateway = user_read_gateway
        self._token_gateway = token_gateway

    async def execute(self, command: LogoutUserCommand) -> None:
        token = await self._token_gateway.get(command.session_id)

        if not token:
            raise SessionNotFoundException
        await self._token_gateway.delete(command.session_id)
