from pydantic import BaseModel, EmailStr


class UserReadResponse(BaseModel):
    email: EmailStr
