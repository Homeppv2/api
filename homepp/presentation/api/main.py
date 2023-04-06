from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastapi.middleware.cors import CORSMiddleware

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
    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        allow_origins=["*"],
    )
    app.include_router(devices_router)
    app.include_router(users_router)

    deps.setup(app)
    exc_handlers.setup(app)

    return app
