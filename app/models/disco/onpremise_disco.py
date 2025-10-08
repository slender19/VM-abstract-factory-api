from typing import Dict
from .disco_base import Disco

class OnPremiseDisco(Disco):
    """Disco físico para entorno local."""

    def __init__(self, tipo_disco: str, capacidad_gb: int, interfaz: str):
        super().__init__("OnPremise Disco")
        self.tipo_disco = tipo_disco
        self.capacidad_gb = capacidad_gb
        self.interfaz = interfaz

    def get_info(self) -> Dict:
        return {
            "tipo": self.tipo,
            "tipo_disco": self.tipo_disco,
            "capacidad_gb": self.capacidad_gb,
            "interfaz": self.interfaz
        }
