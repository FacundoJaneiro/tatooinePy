from sqlalchemy import ForeignKey
from Entities.sistemaDeMedida import SistemaDeMedida
from config import db


class UnidadMedida(db.Model):
    __tablename__ = 'unidadesdemedida'
    PK_unidadMedida = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombreUnidadMedida = db.Column(db.String(30))
    denominacionUnidadMedida = db.Column(db.String(30))
    factorUnidadMedida = db.Column(db.Float)
    FK_sistemaMedida = db.Column(db.Integer, ForeignKey('sistemademedida.Pk_sistemaDeMedida'))
    statusUnidadesMedidas = db.Column(db.Integer)
    sistemaDeMedida = db.relationship("SistemaDeMedida", backref=db.backref("unidadesdemedida", lazy='dynamic'))