from typing import Dict
from .disco_base import Disco

class AzureDisco(Disco):
    """Disco para Azure."""

    def __init__(self, tipo_disco: str, capacidad_gb: int, redundancia: str):
        super().__init__("Azure Disco")
        self.tipo_disco = tipo_disco
        self.capacidad_gb = capacidad_gb
        self.redundancia = redundancia

    def get_info(self) -> Dict:
        return {
            "tipo": self.tipo,
            "tipo_disco": self.tipo_disco,
            "capacidad_gb": self.capacidad_gb,
            "redundancia": self.redundancia
        }
