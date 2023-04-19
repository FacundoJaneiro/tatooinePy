from Exceptions.baseException import BaseException


class TokenNotFoundException(BaseException):
    def __init__(self):
        super().__init__()
        self.message = "Token not Found"
        self.statusCode = 401
