from Exceptions.baseException import BaseException


class ParameterNotFoundException(BaseException):
    def __init__(self, parametro):
        super().__init__()
        self.message = f"Parametro incorrecto: {parametro}"
        self.statusCode = 400