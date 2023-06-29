from Repositories.ComponenteRepository import ComponenteRepository
from Services.interfazComponenteService import InterfazComponenteService


class ComponenteService(InterfazComponenteService):
    def __init__(self):
        self.componenteRepository = ComponenteRepository()

    def getAll(self,tipo):
        componentes = self.componenteRepository.getAll(tipo)
        return componentes

    def getId(self):
        pass

    def save(self):
        pass

    def delete(self):
        pass

    def modify(self):
        pass
