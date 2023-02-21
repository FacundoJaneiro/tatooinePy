from abc import ABC, abstractmethod
from typing import List

from Entities.usuario import User


class InterfazUsuarioService(ABC):
    @abstractmethod
    def getAll(self) -> List[User]:
        pass

    @abstractmethod
    def getId(self) -> User:
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def delete(self):
        pass
