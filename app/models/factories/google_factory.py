from typing import Dict
from .factory_interface import ProveedorFactory
from ..vm.google_vm import GoogleVM
from ..red.google_red import GoogleRed
from ..disco.google_disco import GoogleDisco

class GoogleFactory(ProveedorFactory):
    """Fábrica concreta para Google Cloud."""

    def crear_vm(self, parametros: Dict) -> GoogleVM:
        return GoogleVM(
            machine_type=parametros.get("machine_type", "e2-medium"),
            zona=parametros.get("zona", "us-central1-a"),
            disco_base=parametros.get("disco_base", "pd-standard"),
            proyecto=parametros.get("proyecto", "default-proj")
        )

    def crear_red(self, parametros: Dict) -> GoogleRed:
        return GoogleRed(
            network_name=parametros.get("network_name", "default-net"),
            subred=parametros.get("subred", "default-subnet"),
            proyecto=parametros.get("proyecto", "default-proj")
        )

    def crear_disco(self, parametros: Dict) -> GoogleDisco:
        return GoogleDisco(
            disk_type=parametros.get("disk_type", "pd-ssd"),
            size_gb=parametros.get("size_gb", 100),
            zone=parametros.get("zone", "us-central1-a")
        )
