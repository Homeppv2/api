from fastapi import FastAPI

from .mediator import provide_mediator, provide_mediator_stub


def setup(app: FastAPI):
    app.dependency_overrides = {
        provide_mediator_stub: provide_mediator,
    }
