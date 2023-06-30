from Exceptions.baseException import BaseException


class ComponenteNotFoundException(BaseException):
    def __init__(self):
        super().__init__()
        self.message = "No se encontró el componente"
        self.statusCode = 404