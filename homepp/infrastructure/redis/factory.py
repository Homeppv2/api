from redis.asyncio import Redis

from homepp.config.settings import Settings


def build_redis(settings: Settings):
    return Redis(host=settings.redis.host, port=settings.redis.port)
