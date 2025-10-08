from typing import Dict
from .vm_base import VM

class OnPremiseVM(VM):
    """Máquina virtual local."""

    def __init__(self, cpu: int, ram: int, disco: int, red_fisica: str):
        super().__init__("OnPremise VM")
        self.cpu = cpu
        self.ram = ram
        self.disco = disco
        self.red_fisica = red_fisica

    def get_info(self) -> Dict:
        return {
            "tipo": self.tipo,
            "cpu": self.cpu,
            "ram": self.ram,
            "disco": self.disco,
            "red_fisica": self.red_fisica
        }
