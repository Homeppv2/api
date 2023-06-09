from fastapi import APIRouter

from .http import create_user, login, logout, current

router = APIRouter(
    prefix="/users",
)
router.include_router(create_user.router)
router.include_router(login.router)
router.include_router(logout.router)
router.include_router(current.router)
