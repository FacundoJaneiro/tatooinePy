from abc import ABC, abstractmethod
from typing import List
from Entities.componente import Componente


class InterfazComponenteService(ABC):
    @abstractmethod
    def getAll(self) -> List[Componente]:
        pass

    @abstractmethod
    def getId(self) -> Componente:
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def modify(self):
        pass

