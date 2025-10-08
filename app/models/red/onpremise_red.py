from typing import Dict
from .red_base import Red

class OnPremiseRed(Red):
    """Red física local."""

    def __init__(self, nombre_switch: str, ip_gateway: str, vlan_id: int):
        super().__init__("OnPremise Red")
        self.nombre_switch = nombre_switch
        self.ip_gateway = ip_gateway
        self.vlan_id = vlan_id

    def get_info(self) -> Dict:
        return {
            "tipo": self.tipo,
            "nombre_switch": self.nombre_switch,
            "ip_gateway": self.ip_gateway,
            "vlan_id": self.vlan_id
        }
