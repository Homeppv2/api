from typing import Protocol, Optional

from homepp.core.common.types.user import UserId, Username, Email, RawPassword
from homepp.core.user.domain.models import User


class UserProtocol(Protocol):
    name: Username
    email: Email
    hashed_password: RawPassword


class UserWriteGateway:
    def __init__(self, db):
        self.db = db

    def create_user(self, user_gateway: UserProtocol) -> UserProtocol:
        user = User(name=self.name, email=self.email, hashed_password=self.hashed_password)
        self.db.add(user)
        self.db.commit()
        return user

class UserReadGateway:
    def __init__(self, db):
        self.db = db

    async def get_user_by_id(self, user_id: UserId) -> Optional[User]:
        return self.db.query(User).filter(User.id == user_id).first()

    async def get_user_by_email(self, email: Email) -> Optional[User]:
        return self.db.query(User).filter(User.email == email).first()

    # Разве у User должно быть поле hw_key ?
    async def get_by_hw_key(self, hw_key: str) -> Optional[User]:
        raise NotImplementedError
