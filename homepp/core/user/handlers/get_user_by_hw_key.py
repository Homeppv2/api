from dataclasses import dataclass

from homepp.core.common.handler import Handler
from homepp.core.common.exc.user import UserDoesNotExistsException
from homepp.core.user.domain.models import User
from homepp.core.user.protocols.user_gateway import UserReadGateway


@dataclass
class GetUserByHwKeyCommand:
    hw_key: str


class GetUserByHwKeyHandler(Handler[GetUserByHwKeyCommand, User]):
    def __init__(self, user_read_gateway: UserReadGateway) -> None:
        self._user_reader = user_read_gateway

    async def execute(self, command: GetUserByHwKeyCommand) -> User:
        user = await self._user_reader.get_by_hw_key(command.hw_key)

        if not user:
            raise UserDoesNotExistsException

        return user
