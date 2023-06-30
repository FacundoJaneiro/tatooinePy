from Exceptions.baseException import BaseException


class InvalidTokenException(BaseException):
    def __init__(self):
        super().__init__()
        self.message = "Invalid token"
        self.statusCode = 401
