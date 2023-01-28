from Entities.usuario import User
from Exceptions.userNotFoundException import UserNotFoundException


class UsuarioRepository():

    def getAll(self):
        users = User.query.all()
        return users

    def getId(self, id):
        user = User.query.filter_by(PK_usuario=id).first()
        if user is None:
            raise UserNotFoundException
        return user
