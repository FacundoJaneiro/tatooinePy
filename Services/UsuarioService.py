from Repositories.UsuarioRepository import UsuarioRepository
from Services.interfazUsuarioService import InterfazUsuarioService
from werkzeug.security import generate_password_hash, check_password_hash
from Exceptions.userPasswordNotFoundException import UserPasswordNotFoundException
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
        userToModify = self.usuarioRepository.getId(user.PK_usuario)
        user_dict = vars(user)
        for Attr, Value in user_dict.items():
            if not Attr.startswith('_') and Value is not None:
                setattr(userToModify, Attr, Value)

        self.usuarioRepository.modify()

    def login(self, user):
        userToCheck = self.usuarioRepository.searchEmail(user.emailUsuario)
        if check_password_hash(userToCheck.passwordUsuario, user.passwordUsuario):
            # Aqui desarrollo la logica del token
            token = 'TokenUltraSecretElCualNuncaPodrasSaber'
            userToCheck.token = token
        else:
            raise UserPasswordNotFoundException

        return token
