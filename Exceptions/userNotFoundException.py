from Exceptions.baseException import BaseException


class UserNotFoundException(BaseException):
    def __init__(self):
        super().__init__()
        self.message = "No se encontró un usuario con ese ID"
        self.statusCode = 404
