from Exceptions.baseException import BaseException


class MissingDataRequiredException(BaseException):
    def __init__(self):
        super().__init__()
        self.message = "Faltan Datos Obligatorios"
        self.statusCode = 400
