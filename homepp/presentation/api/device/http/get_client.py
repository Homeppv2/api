from fastapi import APIRouter

from .models.response import GetClientResponse

router = APIRouter()


# TODO: implement the method and add user validation
# bring business logic to the core
@router.get(
    "/client",
)
async def get_client(hw_key: str) -> GetClientResponse:
    return GetClientResponse(client_id="123")
