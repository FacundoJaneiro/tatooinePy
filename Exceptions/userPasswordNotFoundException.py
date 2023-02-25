from Exceptions.baseException import BaseException


class UserPasswordNotFoundException(BaseException):
    def __init__(self):
        super().__init__()
        self.message = "Authentication failed: incorrect password provided. Please try again with the correct password."
        self.statusCode = 401
