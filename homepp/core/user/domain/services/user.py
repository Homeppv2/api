from ..models import User
from homepp.core.common.types.user import Username, Email


class UserService:
    def create(
        self, username: Username, email: Email, hashed_password: str
    ) -> User:
        return User(username, email, hashed_password)
