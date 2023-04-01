from typing import Optional
from redis.asyncio import Redis

from homepp.core.common.types.auth import SessionId
from homepp.core.user.protocols.token_gateway import TokenGateway


class TokenGatewayImpl(TokenGateway):
    def __init__(self, redis: Redis) -> None:
        self._redis = redis

    async def create(self, session_id: SessionId, token: str) -> None:
        await self._redis.set(str(session_id), token)

    async def delete(self, session_id: SessionId) -> None:
        await self._redis.delete(str(session_id))

    async def get(self, session_id: SessionId) -> Optional[str]:
        return await self._redis.get(str(session_id))
