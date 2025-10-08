from typing import Dict
from .disco_base import Disco

class GoogleDisco(Disco):
    """Disco para Google Cloud."""

    def __init__(self, disk_type: str, size_gb: int, zone: str):
        super().__init__("Google Disco")
        self.disk_type = disk_type
        self.size_gb = size_gb
        self.zone = zone

    def get_info(self) -> Dict:
        return {
            "tipo": self.tipo,
            "disk_type": self.disk_type,
            "size_gb": self.size_gb,
            "zone": self.zone
        }
