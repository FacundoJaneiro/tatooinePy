from abc import ABC, abstractmethod
from Entities.usuario import User


class InterfazUsuarioService(ABC):

    @abstractmethod
    def getId(self) -> User:
        pass
