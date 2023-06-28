from Entities.materiaPrima import MateriaPrima
from config import db
from sqlalchemy import text


class MateriaPrimaRepository():

    def getAll(self):
        materiasPrimas = MateriaPrima.query.filter_by(status=1, tipo=1)
        materiasPrimas = materiasPrimas.filter(text(""))
        return materiasPrimas

    def getId(self, id):
        pass

    def save(self, user):
        pass

    def delete(self, user):
        pass

    def modify(self):
        pass
