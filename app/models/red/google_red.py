from typing import Dict
from .red_base import Red

class GoogleRed(Red):
    """Red virtual para Google Cloud."""

    def __init__(self, network_name: str, subred: str, proyecto: str):
        super().__init__("Google Red")
        self.network_name = network_name
        self.subred = subred
        self.proyecto = proyecto

    def get_info(self) -> Dict:
        return {
            "tipo": self.tipo,
            "network_name": self.network_name,
            "subred": self.subred,
            "proyecto": self.proyecto
        }
