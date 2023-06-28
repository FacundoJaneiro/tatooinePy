from abc import ABC, abstractmethod
from typing import List
from Entities.materiaPrima import MateriaPrima


class InterfazMateriaPrimaService(ABC):
    @abstractmethod
    def getAll(self) -> List[MateriaPrima]:
        pass

    @abstractmethod
    def getId(self) -> MateriaPrima:
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

