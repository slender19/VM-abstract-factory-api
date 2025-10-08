from abc import ABC, abstractmethod
from typing import Dict

class VM(ABC):
    """Clase base para Máquinas Virtuales."""

    def __init__(self, tipo: str):
        self.tipo = tipo

    @abstractmethod
    def get_info(self) -> Dict:
        """Devuelve los datos descriptivos de la VM."""
        pass
