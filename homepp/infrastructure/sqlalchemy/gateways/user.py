from sqlalchemy.sql import select

from homepp.core.common.types.user import UserId, Email
from homepp.core.user.protocols.user_gateway import UserWriteGateway, UserReadGateway
from .base import SqlalchemyGateway
from ..models import User as UserModel


class UserGatewayWrite(SqlalchemyGateway, UserWriteGateway):
    async def create_user(self, user: UserId, username: str):
        db_user = UserModel(id=user_id, name=username)
        self._session.add(db_user)
        await self._try_flush()

class UserGatewayRead(SqlalchemyGateway, UserReadGateway):
    async def get_user_by_id(self, user_id: UserId):
        result = await self._session.execute(
            select(UserModel).where(UserModel.id == user_id)  # type: ignore
        )
        return result.scalars().first()

    async def get_user_by_email(self, email: Email):
        result = await self._session.execute(
            select(UserModel).where(UserModel.email == email)  # type: ignore
        )
        return result.scalars().first()