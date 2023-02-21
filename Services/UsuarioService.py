from Repositories.UsuarioRepository import UsuarioRepository
from Services.interfazUsuarioService import InterfazUsuarioService
from werkzeug.security import generate_password_hash
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
        hashed_password = generate_password_hash(user.passwordUsuario)
        user.passwordUsuario = hashed_password
        self.usuarioRepository.save(user)

    def delete(self, id):
        self.usuarioRepository.delete(id)

    def modify(self, user):
        self.usuarioRepository.modify(user)
