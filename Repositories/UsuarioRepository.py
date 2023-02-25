from Entities.usuario import User
from config import db


class UsuarioRepository():

    def getAll(self):
        users = User.query.filter_by(statusUsuario=1)
        return users

    def getId(self, id):
        user = User.query.filter_by(PK_usuario=id, statusUsuario=1).first()
        return user


    def save(self, user):
        db.session.add(user)
        db.session.commit()

    def delete(self, user):
        user.statusUsuario = 0
        db.session.commit()

    def modify(self):
        db.session.commit()

    def searchEmail(self, email):
        user = User.query.filter_by(emailUsuario=email, statusUsuario=1).first()
        return user


