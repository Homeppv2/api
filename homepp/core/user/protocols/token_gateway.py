from typing import Protocol, Optional

from homepp.core.common.types.auth import SessionId


class TokenGateway(Protocol):
    async def create(self, session_id: SessionId, token: str) -> None:
        raise NotImplementedError

    async def delete(self, session_id: SessionId) -> None:
        raise NotImplementedError

    async def get(self, session_id: SessionId) -> Optional[str]:
        raise NotImplementedError
