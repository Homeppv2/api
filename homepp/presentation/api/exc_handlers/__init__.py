from fastapi import FastAPI
from .auth import setup_auth_exc_handlers


def setup(app: FastAPI):
    setup_auth_exc_handlers(app)
