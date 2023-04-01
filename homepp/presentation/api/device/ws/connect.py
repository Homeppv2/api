import json
import aio_pika
from fastapi import APIRouter, Depends
from starlette.websockets import WebSocket
from websockets.exceptions import ConnectionClosed

from homepp.config.settings import get_settings, Settings

router = APIRouter()


# TODO:
# add message processing,
# move the queue to the infrastructure,
# add a connection manager and check for disconnection
# remove client_id from arguments, make getting client id from cookie
# make dependency on checking user authorization via cookies

@router.websocket("/connect/ws")
async def controller_connect(
    client_id: str,
    websocket: WebSocket,
    settings: Settings = Depends(get_settings),
):
    await websocket.accept()
    connection = await aio_pika.connect_robust(settings.rabbit.url)
    async with connection.channel() as channel:
        queue = await channel.declare_queue(
            f"client_{client_id}", durable=True
        )
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
