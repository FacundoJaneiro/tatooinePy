from Entities.usuario import User
from Exceptions.userNotFoundException import UserNotFoundException
from config import db


class UsuarioRepository():

    def getAll(self):
        users = User.query.filter_by(statusUsuario=1)
        return users

    def getId(self, id):
        user = User.query.filter_by(PK_usuario=id, statusUsuario=1).first()
        if user is None:
            raise UserNotFoundException
        return user

    def save(self, user):
        db.session.add(user)
        db.session.commit()

    def delete(self, id):
        user = User.query.filter_by(PK_usuario=id, statusUsuario=1).first()
        if user is None:
            raise UserNotFoundException
        else:
            user.statusUsuario = 0
            db.session.commit()

