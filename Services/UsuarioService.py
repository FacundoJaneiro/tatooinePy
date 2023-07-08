from Exceptions.userNotFoundException import UserNotFoundException
from Repositories.UsuarioRepository import UsuarioRepository
from Services.interfazUsuarioService import InterfazUsuarioService
from werkzeug.security import generate_password_hash, check_password_hash
from Exceptions.userPasswordNotFoundException import UserPasswordNotFoundException
from Exceptions.emailAlredyExistsException import EmailAlreadyExistsException


class UsuarioService(InterfazUsuarioService):
    def __init__(self):
        self.usuarioRepository = UsuarioRepository()

    def getAll(self,filtros):
        users = self.usuarioRepository.getAll(filtros)
        return users

    def getId(self, id):
        user = self.usuarioRepository.getId(id)
        if user is None:
            raise UserNotFoundException
        return user

    def save(self, user):
        userSearchEmail = self.usuarioRepository.searchEmail(user.emailUsuario)
        if userSearchEmail:
            raise EmailAlreadyExistsException
        hashed_password = generate_password_hash(user.passwordUsuario)
        user.passwordUsuario = hashed_password
        self.usuarioRepository.save(user)

    def delete(self, id):
        userToDelete = self.usuarioRepository.getId(id)
        if userToDelete is None:
            raise UserNotFoundException
        else:
            self.usuarioRepository.delete(userToDelete)

    def modify(self, user):
        userToModify = self.usuarioRepository.getId(user.PK_usuario)
        if userToModify is None:
            raise UserNotFoundException
        user_dict = vars(user)
        for Attr, Value in user_dict.items():
            if not Attr.startswith('_') and Value is not None:
                setattr(userToModify, Attr, Value)

        self.usuarioRepository.modify()

    def login(self, user):
        userToCheck = self.usuarioRepository.searchEmail(user.emailUsuario)
        if userToCheck is None:
            raise UserNotFoundException
        if check_password_hash(userToCheck.passwordUsuario, user.passwordUsuario):

            info = {'id': userToCheck.PK_usuario,
                    'username': userToCheck.nombreUsuario + ' ' + userToCheck.apellidoUsuario,
                    'rol': userToCheck.rol.descripcionRol
                    }

        else:
            raise UserPasswordNotFoundException

        return info
