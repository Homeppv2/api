from pydantic import BaseModel, EmailStr

from homepp.core.common.types.user import RawPassword


class UserSignUpRequest(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserLoginFormRequest(BaseModel):
    username: str
    password: RawPassword
