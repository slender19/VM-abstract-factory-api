from typing import Dict
from .factory_interface import ProveedorFactory
from ..vm.onpremise_vm import OnPremiseVM
from ..red.onpremise_red import OnPremiseRed
from ..disco.onpremise_disco import OnPremiseDisco

class OnPremiseFactory(ProveedorFactory):
    """Fábrica concreta para entorno local."""

    def crear_vm(self, parametros: Dict) -> OnPremiseVM:
        return OnPremiseVM(
            cpu=parametros.get("cpu", 4),
            ram=parametros.get("ram", 16),
            disco=parametros.get("disco", 256),
            red_fisica=parametros.get("red_fisica", "eth0")
        )

    def crear_red(self, parametros: Dict) -> OnPremiseRed:
        return OnPremiseRed(
            nombre_switch=parametros.get("nombre_switch", "Switch01"),
            ip_gateway=parametros.get("ip_gateway", "192.168.0.1"),
            vlan_id=parametros.get("vlan_id", 10)
        )

    def crear_disco(self, parametros: Dict) -> OnPremiseDisco:
        return OnPremiseDisco(
            tipo_disco=parametros.get("tipo_disco", "SSD"),
            capacidad_gb=parametros.get("capacidad_gb", 500),
            interfaz=parametros.get("interfaz", "SATA")
        )
