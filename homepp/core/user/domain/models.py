from typing import Optional
from dataclasses import dataclass, field

from homepp.core.common.types.user import UserId, Username, Email


@dataclass
class User:
    id: Optional[UserId] = field(init=False, default=None)
    username: Username
    email: Email
    hashed_password: str