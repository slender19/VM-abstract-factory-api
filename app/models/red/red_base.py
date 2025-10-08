from abc import ABC, abstractmethod
from typing import Dict

class Red(ABC):
    """Clase base para redes virtuales."""

    def __init__(self, tipo: str):
        self.tipo = tipo

    @abstractmethod
    def get_info(self) -> Dict:
        """Devuelve los datos de la red."""
        pass
