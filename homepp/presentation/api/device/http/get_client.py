from fastapi import APIRouter, Depends

from homepp.core.user.handlers.get_user_by_hw_key import GetUserByHwKeyCommand
from homepp.core.common.mediator import Mediator
from .models.response import GetClientResponse
from ...deps.mediator import provide_mediator_stub

router = APIRouter()


# TODO: implement the method and add user validation
# bring business logic to the core
@router.get(
    "/client",
)
async def get_client(
    hw_key: str, mediator: Mediator = Depends(provide_mediator_stub)
) -> GetClientResponse:
    user = await mediator.send(GetUserByHwKeyCommand(hw_key))
    return GetClientResponse(client_id=user.id)
