from Entities.usuario import User


class UsuarioRepository():

    def getAll(self):
        users = User.query.all()
        return users

    def getId(self, id):
        user = User.query.filter_by(PK_usuario=id).first()
        return user
