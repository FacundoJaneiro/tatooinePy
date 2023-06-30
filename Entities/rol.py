from config import db


class Rol(db.Model):
    __tablename__ = 'roles'
    PK_rol = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descripcionRol = db.Column(db.String(30))

