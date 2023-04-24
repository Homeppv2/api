class ApplicationException(Exception):
    ...


class ValidationError(ApplicationException):
    """Raised when a validation error occurs"""

    def __init__(self, message: str):
        self.message = message


class UniqueConstraintViolation(ApplicationException):
    """Raised when a unique constraint is violated"""
