from Entities.usuario import User
from config import db
from sqlalchemy import text
from Repositories.FilterCreator import FilterCreator


class UsuarioRepository():

    def __init__(self):
        self.filtersKeys = {
            'nombreUsuario': 'equal',
            'apellidoUsuario': 'equal',
            'emailUsuario': 'equal',
            'FK_rol': 'equal',
        }
        self.filterCreator = FilterCreator(self.filtersKeys)

    def getAll(self,filtros):
        filter = self.filterCreator.createFilter(filtros)
        users = db.session.query(User).filter(text(filter))
        users = users.filter_by(statusUsuario=1)
        users = users.filter(text(""))
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
