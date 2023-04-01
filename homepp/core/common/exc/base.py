class ApplicationException(Exception):
    ...


class ValidationError(ApplicationException):
    """Raised when a validation error occurs"""


class UniqueConstraintViolation(ApplicationException):
    """Raised when a unique constraint is violated"""
