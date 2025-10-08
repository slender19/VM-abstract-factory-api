from abc import ABC, abstractmethod
from typing import Dict

class Disco(ABC):
    """Clase base para discos virtuales."""

    def __init__(self, tipo: str):
        self.tipo = tipo

    @abstractmethod
    def get_info(self) -> Dict:
        """Devuelve la información del disco."""
        pass
