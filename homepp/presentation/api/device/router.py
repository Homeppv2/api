from fastapi import APIRouter

from .http.get_client import router as http_get_client_router
from .ws.connect import router as ws_connect_router

router = APIRouter(prefix="/controllers", tags=["Controllers"])
router.include_router(http_get_client_router)
router.include_router(ws_connect_router)
