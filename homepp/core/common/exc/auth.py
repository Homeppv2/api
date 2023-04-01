from .base import ApplicationException


class InvalidTokenException(ApplicationException):
    """Invalid token exception."""


class InvalidCredentialsException(ApplicationException):
    """Invalid credentials exception."""


class SessionNotFoundException(ApplicationException):
    """Session not found exception."""
