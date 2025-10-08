from typing import Dict
from .red_base import Red

class AWSRed(Red):
    """Red virtual para AWS."""

    def __init__(self, vpc_id: str, subnet: str, security_group: str):
        super().__init__("AWS Red")
        self.vpc_id = vpc_id
        self.subnet = subnet
        self.security_group = security_group

    def get_info(self) -> Dict:
        return {
            "tipo": self.tipo,
            "vpc_id": self.vpc_id,
            "subnet": self.subnet,
            "security_group": self.security_group
        }
