from Exceptions.baseException import BaseException


class UserNotFoundException(BaseException):
    def __init__(self):
        super().__init__()
        self.message = "No se encontró un usuario"
        self.statusCode = 404
