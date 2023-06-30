from config import db


class SistemaDeMedida(db.Model):
    __tablename__ = 'sistemademedida'
    Pk_sistemaDeMedida = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombreSistMedida = db.Column(db.String(30))
    statusSistMedida = db.Column(db.Integer)
