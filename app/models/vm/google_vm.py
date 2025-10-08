from typing import Dict
from .vm_base import VM

class GoogleVM(VM):
    """Máquina virtual para Google Cloud."""

    def __init__(self, machine_type: str, zona: str, disco_base: str, proyecto: str):
        super().__init__("Google VM")
        self.machine_type = machine_type
        self.zona = zona
        self.disco_base = disco_base
        self.proyecto = proyecto

    def get_info(self) -> Dict:
        return {
            "tipo": self.tipo,
            "machine_type": self.machine_type,
            "zona": self.zona,
            "disco_base": self.disco_base,
            "proyecto": self.proyecto
        }
