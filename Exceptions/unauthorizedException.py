from Exceptions.baseException import BaseException


class UnauthorizedException(BaseException):
    def __init__(self):
        super().__init__()
        self.message = "Unauthorized"
        self.statusCode = 401
