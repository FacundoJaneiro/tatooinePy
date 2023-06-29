from Entities.componente import Componente
from config import db
from sqlalchemy import text


class ComponenteRepository():

    def getAll(self,tipo):
        componente = Componente.query.filter_by(status=1, tipo=tipo)
        componente = componente.filter(text(""))
        return componente

    def getId(self, tipo, id):
        componente = Componente.query.filter_by(PK_componente=id, status=1, tipo=tipo).first()
        return componente

    def save(self, componente):
        db.session.add(componente)
        db.session.commit()

    def delete(self, user):
        pass

    def modify(self):
        db.session.commit()
