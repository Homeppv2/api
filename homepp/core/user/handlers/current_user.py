import uuid
from dataclasses import dataclass

from homepp.core.common.handler import Handler
from homepp.core.common.uow import UnitOfWork
from homepp.core.common.types.user import UserId
from homepp.core.common.types.auth import SessionId
from homepp.core.user.domain.models import User
from homepp.core.user.protocols.user_gateway import UserReadGateway
from homepp.core.user.protocols.token_gateway import TokenGateway
from homepp.core.user.domain.services.auth import AuthUserService
from homepp.core.common.exc.auth import SessionNotFoundException


@dataclass
class GetCurrentUserCommand:
    session_id: SessionId


class GetCurrentUserHandler(Handler[GetCurrentUserCommand, User]):
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

    async def execute(self, command: GetCurrentUserCommand) -> User:
        token = await self._token_gateway.get(command.session_id)
        if not token:
            raise SessionNotFoundException

        user_id = UserId(uuid.UUID(self._auth_service.decode_token(token)))
        user = await self._user_read_gateway.get_user_by_id(user_id)
        return user  # type: ignore
