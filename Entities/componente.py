from sqlalchemy import ForeignKey
from Entities.rubros import Rubro
from Entities.unidadDeMedida import UnidadMedida
from config import db


class Componente(db.Model):
    __tablename__ = 'componentes'
    PK_componente = db.Column(db.Integer, primary_key=True, autoincrement=True)
    identificacion = db.Column(db.String(30))
    nombre = db.Column(db.String(50))
    descripcion = db.Column(db.String(120))
    codigo = db.Column(db.String(50))
    status = db.Column(db.Integer)
    stock = db.Column(db.Float)
    stockMinimo = db.Column(db.Float)
    stockVirtual = db.Column(db.Float)
    tipo = db.Column(db.Integer)
    FK_rubro = db.Column(db.Integer, ForeignKey('rubros.PK_rubro'))
    FK_unidadMedida = db.Column(db.Integer, ForeignKey('unidadesdemedida.PK_unidadMedida'))
    rubro = db.relationship("Rubro", backref=db.backref("materiasPrimas", lazy='dynamic'))
    unidadMedida = db.relationship("UnidadMedida", backref=db.backref("materiasPrimas", lazy='dynamic'))
