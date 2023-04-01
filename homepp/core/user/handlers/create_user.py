from dataclasses import dataclass

from homepp.core.common.types.user import Username, Email, RawPassword
from homepp.core.common.handler import Handler
from homepp.core.common.uow import UnitOfWork
from homepp.core.common.exc.base import UniqueConstraintViolation
from homepp.core.common.exc.user import UserAlreadyExistsException
from homepp.core.user.domain.services.user import UserService
from homepp.core.user.domain.services.auth import AuthUserService
from homepp.core.user.protocols.user_gateway import UserWriteGateway


@dataclass
class CreateUserCommand:
    username: str
    email: str
    raw_password: str


class CreateUserHandler(Handler[CreateUserCommand, None]):
    def __init__(
        self,
        user_service: UserService,
        auth_service: AuthUserService,
        user_write_gateway: UserWriteGateway,
        uow: UnitOfWork,
    ) -> None:
        self._user_write_gateway = user_write_gateway
        self._auth_service = auth_service
        self._user_service = user_service
        self._uow = uow

    async def execute(self, command: CreateUserCommand) -> None:
        hashed_password = self._auth_service.hash_pass(
            RawPassword(command.raw_password)
        )
        user = self._user_service.create(
            username=Username(command.username),
            email=Email(command.email),
            hashed_password=hashed_password,
        )
        self._user_write_gateway.create_user(user)
        try:
            await self._uow.commit()
        except UniqueConstraintViolation:
            raise UserAlreadyExistsException
