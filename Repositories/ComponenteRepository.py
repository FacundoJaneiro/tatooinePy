from Entities.componente import Componente
from config import db
from sqlalchemy import text


class ComponenteRepository():

    def getAll(self,tipo):
        componente = Componente.query.filter_by(status=1, tipo=tipo)
        componente = componente.filter(text(""))
        return componente

    def getId(self, id):
        pass

    def save(self, user):
        pass

    def delete(self, user):
        pass

    def modify(self):
        pass
