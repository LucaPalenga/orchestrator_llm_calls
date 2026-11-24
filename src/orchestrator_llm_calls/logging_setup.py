import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

# Il nome del logger deve coincidere con il nome del package
# in questo modo posso utilizzare da fuori logging.getLogger(__name__)
LOGGER_NAME = "orchestrator_llm_calls"
LOG_FILE = Path(__file__).resolve().parent / LOGGER_NAME

def setup_logging(level: str = "INFO", log_dir: Path = Path("logs")) -> logging.Logger:
    """Configura i logger console + file a rotazione."""

    log_dir.mkdir(parents=True, exist_ok=True)

    # Logger principale
    logger = logging.getLogger(LOGGER_NAME)
    logger.setLevel(logging.DEBUG)

    # Se già configurato non aggiungo altri handler 
    if logger.handlers:
        return logger

    # Handler per la console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_formatter = logging.Formatter('%(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)

    # Handler per salvare su file i log in cui vengono registrati tutti i messaggi più dettagliati
    rotating_handler = RotatingFileHandler(
            log_dir / "orchestrator.log", 
            maxBytes=500_000,  
            backupCount=3
        )
    rotating_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s')
    rotating_handler.setFormatter(rotating_formatter)
    
    # Handler per salvare su file gli errori
    error_handler = logging.FileHandler(log_dir / "errors.log")
    error_handler.setLevel(logging.WARNING)
    error_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s')
    error_handler.setFormatter(error_formatter)
    
    logger.addHandler(console_handler)
    logger.addHandler(rotating_handler)
    logger.addHandler(error_handler)

    return logger
