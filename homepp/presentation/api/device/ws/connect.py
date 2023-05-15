import json
import aio_pika
from uuid import UUID
from fastapi import APIRouter, Depends
from starlette.websockets import WebSocket
from websockets.exceptions import ConnectionClosed

# from homepp.core.user.domain.models import User
from homepp.config.settings import get_settings, Settings
from homepp.presentation.api.deps.auth import provide_mediator_stub
from homepp.core.common.mediator import Mediator
from homepp.core.common.types.auth import SessionId
from homepp.core.common.exc.auth import SessionNotFoundException
from homepp.core.user.handlers.current_user import GetCurrentUserCommand
# from ...deps.auth import get_current_user

router = APIRouter()


# TODO:
# move the queue to the infrastructure,
# add a connection manager and check for disconnection


@router.websocket("/connect/ws")
async def controller_connect(
    session_id: str,
    websocket: WebSocket,
    mediator: Mediator = Depends(provide_mediator_stub),
    settings: Settings = Depends(get_settings),
):
    err = False
    if not session_id:
        err = True
    try:
        user = await mediator.send(
            GetCurrentUserCommand(SessionId(UUID(session_id)))
        )
        if not user:
            err = True
    except ValueError:
        err = True

    if err:
        raise SessionNotFoundException

    await websocket.accept()
    connection = await aio_pika.connect_robust(settings.rabbit.url)
    async with connection.channel() as channel:
        queue = await channel.declare_queue(f"client_{user.id}", durable=True)
        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                try:
                    async with message.process():
                        await websocket.send_json(
                            json.loads(message.body.decode("utf-8"))
                        )
                except ConnectionClosed:
                    await websocket.close()
                    await channel.close()
                    await connection.close()
                    break
