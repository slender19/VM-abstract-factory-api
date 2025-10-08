from typing import Dict
from .factory_interface import ProveedorFactory
from ..vm.azure_vm import AzureVM
from ..red.azure_red import AzureRed
from ..disco.azure_disco import AzureDisco

class AzureFactory(ProveedorFactory):
    """Fábrica concreta para Azure."""

    def crear_vm(self, parametros: Dict) -> AzureVM:
        return AzureVM(
            tamaño_maquina=parametros.get("tamaño_maquina", "Standard_B1s"),
            resource_group=parametros.get("resource_group", "grupo-por-defecto"),
            imagen=parametros.get("imagen", "UbuntuLTS"),
            red_virtual=parametros.get("red_virtual", "vnet1")
        )

    def crear_red(self, parametros: Dict) -> AzureRed:
        return AzureRed(
            nombre_red=parametros.get("nombre_red", "red-default"),
            direccion=parametros.get("direccion", "10.0.0.0/24"),
            grupo_recursos=parametros.get("grupo_recursos", "grupo-por-defecto")
        )

    def crear_disco(self, parametros: Dict) -> AzureDisco:
        return AzureDisco(
            tipo_disco=parametros.get("tipo_disco", "Premium_LRS"),
            capacidad_gb=parametros.get("capacidad_gb", 128),
            redundancia=parametros.get("redundancia", "ZRS")
        )
