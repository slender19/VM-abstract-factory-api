from typing import Dict
from .red_base import Red

class AzureRed(Red):
    """Red virtual para Azure."""

    def __init__(self, nombre_red: str, direccion: str, grupo_recursos: str):
        super().__init__("Azure Red")
        self.nombre_red = nombre_red
        self.direccion = direccion
        self.grupo_recursos = grupo_recursos

    def get_info(self) -> Dict:
        return {
            "tipo": self.tipo,
            "nombre_red": self.nombre_red,
            "direccion": self.direccion,
            "grupo_recursos": self.grupo_recursos
        }
