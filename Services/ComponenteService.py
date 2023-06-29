from Repositories.ComponenteRepository import ComponenteRepository
from Services.interfazComponenteService import InterfazComponenteService
from Exceptions.componenteNotFoundException import ComponenteNotFoundException


class ComponenteService(InterfazComponenteService):
    def __init__(self):
        self.componenteRepository = ComponenteRepository()

    def getAll(self,tipo):
        componentes = self.componenteRepository.getAll(tipo)
        return componentes

    def getId(self,tipo,id):
        componente = self.componenteRepository.getId(tipo,id)
        if componente is None:
            raise ComponenteNotFoundException
        return componente

    def save(self, componente):
        self.componenteRepository.save(componente)

    def delete(self):
        pass

    def modify(self, componente):
        componenteToModify = self.componenteRepository.getId(componente.tipo,componente.PK_componente)
        if componenteToModify is None:
            raise ComponenteNotFoundException
        componente_dict = vars(componente)
        for Attr, Value in componente_dict.items():
            if not Attr.startswith('_') and Value is not None:
                setattr(componenteToModify, Attr, Value)

        self.componenteRepository.modify()
