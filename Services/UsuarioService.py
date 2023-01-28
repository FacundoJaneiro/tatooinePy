from Repositories.UsuarioRepository import UsuarioRepository
from Services.interfazUsuarioService import InterfazUsuarioService


class UsuarioService(InterfazUsuarioService):
    def __init__(self):
        self.usuarioRepository = UsuarioRepository()

    def getAll(self):
        users = self.usuarioRepository.getAll()
        return users

    def getId(self, id):
        user = self.usuarioRepository.getId(id)
        return user
