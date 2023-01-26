from sqlalchemy import ForeignKey

from config import db


class User(db.Model):
    __tablename__ = 'usuarios'
    PK_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombreUsuario = db.Column(db.String(30))
    apellidoUsuario = db.Column(db.String(30))
    statusUsuario = db.Column(db.Integer)
    emailUsuario = db.Column(db.String(50), unique=True)
    passwordUsuario = db.Column(db.String(10))
    avatarUsuario = db.Column(db.String(20))
    FK_rol = db.Column(db.Integer, ForeignKey('roles.PK_rol'))

