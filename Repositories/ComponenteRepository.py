from Entities.componente import Componente
from config import db
from sqlalchemy import text
from Repositories.FilterCreator import FilterCreator


class ComponenteRepository():
    def __init__(self):
        self.filtersKeys = {
            'identificacion': 'equal',
            'nombre': 'equal',
            'codigo': 'equal',
            'FK_rubro': 'equal',
        }
        self.filterCreator = FilterCreator(self.filtersKeys)

    def getAll(self,tipo, filtros):
        filter = self.filterCreator.createFilter(filtros)
        componentes = db.session.query(Componente).filter(text(filter))
        componentes = componentes.filter_by(status=1, tipo=tipo)
        componentes = componentes.filter(text(""))
        return componentes

    def getId(self, tipo, id):
        componente = Componente.query.filter_by(PK_componente=id, status=1, tipo=tipo).first()
        return componente

    def save(self, componente):
        db.session.add(componente)
        db.session.commit()

    def delete(self, componente):
        componente.status = 0
        db.session.commit()

    def modify(self):
        db.session.commit()
