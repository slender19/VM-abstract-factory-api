from app.utils.logger import log_event, log_error
from app.factory_provider import FactoryProvider

class ProvisionService:

    @staticmethod
    def aprovisionar(proveedor: str, parametros: dict):
        try:
            log_event(f"Solicitud de aprovisionamiento recibida para proveedor: {proveedor}")

            factory = FactoryProvider.get_factory(proveedor)
            log_event(f"Fábrica seleccionada: {proveedor}")

            vm = factory.crear_vm(parametros.get("vm", {}))
            red = factory.crear_red(parametros.get("red", {}))
            disco = factory.crear_disco(parametros.get("disco", {}))

            
            invalid_fields = {
                "aws": ["tipo_instancia", "region", "vpc", "ami"],
                "azure": ["tamaño_maquina", "resource_group", "imagen", "red_virtual"],
                "google": ["machine_type", "zone", "project"],
                "onpremise": ["cpu", "ram", "disco", "red_fisica"]
            }

            datos_vm = parametros.get("vm", {})
            if datos_vm:
                campos_validos = invalid_fields.get(proveedor, [])
                if not any(campo in datos_vm for campo in campos_validos):
                    log_error(f"Inconsistencia detectada: parámetros de VM no pertenecen a {proveedor}")
                    return {
                        "status": "error",
                        "detalle": "Inconsistencia: la VM no pertenece al proveedor seleccionado.",
                        "estado": "fallido"
                    }

            log_event(f"Recursos aprovisionados correctamente para {proveedor}.")

            return {
                "status": "éxito",
                "proveedor": proveedor,
                "recursos": {
                    "vm": vm.__dict__,
                    "red": red.__dict__,
                    "disco": disco.__dict__
                },
                "estado": "aprovisionado"
            }

        except Exception as e:
            log_error(f"Error en aprovisionamiento ({proveedor}): {e}")
            return {
                "status": "error",
                "detalle": str(e),
                "estado": "fallido"
            }
