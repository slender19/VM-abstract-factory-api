from typing import Dict
from .factory_interface import ProveedorFactory
from ..vm.aws_vm import AWSVM
from ..red.aws_red import AWSRed
from ..disco.aws_disco import AWSDisco

class AWSFactory(ProveedorFactory):
    """Fábrica concreta para AWS (crea VM, Red y Disco)."""

    def crear_vm(self, parametros: Dict) -> AWSVM:
        return AWSVM(
            tipo_instancia=parametros.get("tipo_instancia", "t2.micro"),
            region=parametros.get("region", "us-east-1"),
            vpc=parametros.get("vpc", "vpc-12345"),
            ami=parametros.get("ami", "ami-default")
        )

    def crear_red(self, parametros: Dict) -> AWSRed:
        return AWSRed(
            vpc_id=parametros.get("vpc_id", "vpc-12345"),
            subnet=parametros.get("subnet", "subnet-01"),
            security_group=parametros.get("security_group", "sg-default")
        )

    def crear_disco(self, parametros: Dict) -> AWSDisco:
        return AWSDisco(
            volumeType=parametros.get("volumeType", "gp2"),
            sizeGB=parametros.get("sizeGB", 50),
            encrypted=parametros.get("encrypted", True)
        )
