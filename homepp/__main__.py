import uvicorn

from homepp.config.settings import get_settings
from homepp.presentation.api.main import create_app

app = create_app()

if __name__ == "__main__":
    settings = get_settings()
    uvicorn.run(app=app, host=settings.server.host, port=settings.server.port)
