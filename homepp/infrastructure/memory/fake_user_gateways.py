import uuid
from typing import Optional, List

from homepp.core.common.types.user import UserId, Email
from homepp.core.user.domain.models import User
from homepp.core.user.protocols.user_gateway import (
    UserReadGateway,
    UserWriteGateway,
)


class FakeUserReadGateway(UserReadGateway):
    def __init__(self, users: Optional[List[User]] = None):
        if users is None:
            self.users = []
        else:
            self.users = users

    async def get_user_by_id(self, user_id: UserId) -> Optional[User]:
        for i in self.users:
            if i.id == user_id:
                return i
        return None

    async def get_user_by_email(self, email: Email) -> Optional[User]:
        for i in self.users:
            if i.email == email:
                return i
        return None

    async def get_by_hw_key(self, hw_key: str) -> Optional[User]:
        if self.users:
            return self.users[0]
        return None


class FakeUserWriteGateway(UserWriteGateway):
    def __init__(self, users: Optional[List[User]] = None):
        if users is None:
            self.users = []
        else:
            self.users = users

    def create_user(self, user: User) -> None:
        user.id = UserId(uuid.uuid4())
        self.users.append(user)
