from fastapi import FastAPI, HTTPException
from app.services.provision_service import ProvisionService
from app.utils.logger import log_event

app = FastAPI(
    title="API de Aprovisionamiento de Recursos (Abstract Factory)",
    description="Simula el aprovisionamiento de VM + Red + Disco para distintos proveedores.",
    version="2.0"
)

@app.post("/aprovisionar")
def aprovisionar(payload: dict):
    proveedor = payload.get("proveedor")
    parametros = payload.get("parametros", {})

    if not proveedor:
        raise HTTPException(status_code=400, detail="Debe especificar un proveedor.")

    log_event(f"Solicitud de aprovisionamiento recibida para proveedor: {proveedor}")

    
    resultado = ProvisionService.aprovisionar(proveedor, parametros)

    if resultado["status"] == "error":
        raise HTTPException(status_code=500, detail=resultado["detalle"])

    return resultado
