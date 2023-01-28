from Entities.usuario import User


class UsuarioRepository():

    def getId(self, id):
        user = User.query.filter_by(PK_usuario=id).first()
        return user
