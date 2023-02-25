from Exceptions.baseException import BaseException


class EmailAlreadyExistsException(BaseException):
    def __init__(self):
        super().__init__()
        self.message = "Email Already Exists"
        self.statusCode = 404
