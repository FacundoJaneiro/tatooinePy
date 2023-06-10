from config import db


class Rubro(db.Model):
    __tablename__ = 'rubros'
    PK_rubro = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombreRubro = db.Column(db.String(30))
    statusRubro = db.Column(db.Integer)


