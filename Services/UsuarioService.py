from Repositories.UsuarioRepository import UsuarioRepository
from Services.interfazUsuarioService import InterfazUsuarioService
from Entities.usuario import User


class UsuarioService(InterfazUsuarioService):
    def __init__(self):
        self.usuarioRepository = UsuarioRepository()

    def getAll(self):
        users = self.usuarioRepository.getAll()
        return users

    def getId(self, id):
        user = self.usuarioRepository.getId(id)
        return user

    def save(self, user):
        self.usuarioRepository.save(user)

