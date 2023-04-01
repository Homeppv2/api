from pydantic import BaseModel


class GetClientRequest(BaseModel):
    hardware_key: str
