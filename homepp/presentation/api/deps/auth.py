from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

from homepp.core.common.types.user import RawPassword
from ..user.http.models.request import UserLoginFormRequest


def get_login_form(
    user: OAuth2PasswordRequestForm = Depends(),
) -> UserLoginFormRequest:
    return UserLoginFormRequest(
        username=user.username,
        password=RawPassword(user.password),
    )
