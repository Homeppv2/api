from pydantic import BaseModel


class GetClientResponse(BaseModel):
    client_id: str
