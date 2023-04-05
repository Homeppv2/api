from .base import ApplicationException


class UserAlreadyExistsException(ApplicationException):
    """User already exists exception"""


class UserDoesNotExistsException(ApplicationException):
    """User does not exist exception"""
