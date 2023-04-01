from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from homepp.presentation.api import deps
from homepp.presentation.api import exc_handlers
from homepp.presentation.api.user.router import router as users_router
from homepp.presentation.api.device.router import router as devices_router


def create_app() -> FastAPI:
    app = FastAPI(
        docs_url="/api/docs",
        openapi_url="/api/openapi.json",
        default_response_class=ORJSONResponse,
    )
    app.include_router(devices_router)
    app.include_router(users_router)

    deps.setup(app)
    exc_handlers.setup(app)

    return app
