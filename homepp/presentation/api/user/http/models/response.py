from pydantic import BaseModel, EmailStr


class UserReadResponse(BaseModel):
    email: EmailStr


class UserResponse(BaseModel):
    username: str
    email: EmailStr
