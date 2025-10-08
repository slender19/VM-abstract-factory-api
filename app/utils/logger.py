import logging
import os


os.makedirs("logs", exist_ok=True)


logging.basicConfig(
    filename="logs/provisioning.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

def log_event(message: str):
    """Registra un evento informativo."""
    logging.info(message)
    print(f"[INFO] {message}")

def log_error(message: str):
    """Registra un error."""
    logging.error(message)
    print(f"[ERROR] {message}")
