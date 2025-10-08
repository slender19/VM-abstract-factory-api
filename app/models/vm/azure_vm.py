from typing import Dict
from .vm_base import VM

class AzureVM(VM):
    """Máquina virtual para Azure."""

    def __init__(self, tamaño_maquina: str, resource_group: str, imagen: str, red_virtual: str):
        super().__init__("Azure VM")
        self.tamaño_maquina = tamaño_maquina
        self.resource_group = resource_group
        self.imagen = imagen
        self.red_virtual = red_virtual

    def get_info(self) -> Dict:
        return {
            "tipo": self.tipo,
            "tamaño_maquina": self.tamaño_maquina,
            "resource_group": self.resource_group,
            "imagen": self.imagen,
            "red_virtual": self.red_virtual
        }
