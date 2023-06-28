from Repositories.MateriasPrimasRepository import MateriaPrimaRepository
from Services.interfazMateriasPrimasService import InterfazMateriaPrimaService


class MateriaPrimaService(InterfazMateriaPrimaService):
    def __init__(self):
        self.materiaPrimaRepository = MateriaPrimaRepository()

    def getAll(self):
        materiasPrimas = self.materiaPrimaRepository.getAll()
        return materiasPrimas

    def getId(self):
        pass

    def save(self):
        pass

    def delete(self):
        pass

    def modify(self):
        pass
