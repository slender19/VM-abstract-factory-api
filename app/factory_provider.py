from app.utils.logger import log_event, log_error
from app.models.factories.aws_factory import AWSFactory
from app.models.factories.azure_factory import AzureFactory
from app.models.factories.google_factory import GoogleFactory
from app.models.factories.onpremise_factory import OnPremiseFactory


class FactoryProvider:
    """Selecciona la fábrica adecuada según el proveedor solicitado."""

    factories = {
        "aws": AWSFactory(),
        "azure": AzureFactory(),
        "google": GoogleFactory(),
        "onpremise": OnPremiseFactory(),
    }

    @classmethod
    def get_factory(cls, provider: str):
        """Devuelve la fábrica correspondiente según el nombre del proveedor."""
        provider = provider.lower()
        if provider not in cls.factories:
            log_error(f"Proveedor desconocido: {provider}")
            raise ValueError(f"Proveedor no soportado: {provider}")

        log_event(f"Fábrica seleccionada: {provider}")
        return cls.factories[provider]
