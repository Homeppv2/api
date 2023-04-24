from fastapi import Depends
from redis.asyncio import Redis

from homepp.config.settings import Settings, get_settings
from homepp.core.common.mediator import Mediator
from homepp.core.user.protocols.token_gateway import TokenGateway

from homepp.infrastructure.redis.token_gateway import TokenGatewayImpl
from homepp.infrastructure.redis.factory import build_redis
from homepp.infrastructure.mediator.factory import build_mediator
from homepp.infrastructure.memory.fake_uow import FakeUnitOfWork
from homepp.infrastructure.memory.fake_user_gateways import (
    FakeUserReadGateway,
    FakeUserWriteGateway,
)

# TODO: make sqlalchemy support
users = []  # type: ignore


def provide_redis(settings: Settings = Depends(get_settings)) -> Redis:
    return build_redis(settings)


def provide_tokens_gateway(
    redis: Redis = Depends(provide_redis),
) -> TokenGateway:
    return TokenGatewayImpl(redis)


def provide_mediator(
    tokens_gateway: TokenGateway = Depends(provide_tokens_gateway),
    settings: Settings = Depends(get_settings),
) -> Mediator:
    # TODO: Implement with sqlalchemy
    fake_user_read_gateway = FakeUserReadGateway(users)
    fake_user_write_gateway = FakeUserWriteGateway(users)
    uow = FakeUnitOfWork()

    mediator = build_mediator(
        fake_user_write_gateway,
        fake_user_read_gateway,
        uow,
        tokens_gateway,
        settings.secret_key,
        settings.token_expiration,
    )
    return mediator


def provide_mediator_stub() -> Mediator:
    raise NotImplementedError
