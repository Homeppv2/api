from typing import Protocol, Optional

from homepp.core.common.types.user import UserId, Email
from homepp.core.user.domain.models import User


class UserWriteGateway(Protocol):
    def create_user(self, user: User) -> None:
        raise NotImplementedError


class UserReadGateway(Protocol):
    async def get_user_by_id(self, user_id: UserId) -> Optional[User]:
        raise NotImplementedError

    async def get_user_by_email(self, email: Email) -> Optional[User]:
        raise NotImplementedError

    async def get_by_hw_key(self, hw_key: str) -> Optional[User]:
        raise NotImplementedError
