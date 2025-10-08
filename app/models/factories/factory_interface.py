from abc import ABC, abstractmethod


class ProveedorFactory(ABC):
    @abstractmethod
    def crear_vm(self, parametros: dict):
        pass

    @abstractmethod
    def crear_red(self, parametros: dict):
        pass

    @abstractmethod
    def crear_disco(self, parametros: dict):
        pass
