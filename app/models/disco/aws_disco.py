from typing import Dict
from .disco_base import Disco

class AWSDisco(Disco):
    """Disco para AWS."""

    def __init__(self, volumeType: str, sizeGB: int, encrypted: bool):
        super().__init__("AWS Disco")
        self.volumeType = volumeType
        self.sizeGB = sizeGB
        self.encrypted = encrypted

    def get_info(self) -> Dict:
        return {
            "tipo": self.tipo,
            "volumeType": self.volumeType,
            "sizeGB": self.sizeGB,
            "encrypted": self.encrypted
        }
