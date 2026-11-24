from orchestrator_llm_calls.logging_setup import setup_logging

log = setup_logging("DEBUG")  
setup_logging("DEBUG")  # verifica che non si duplichi
print(__name__)
log.debug("solo dettaglio")
log.warning("deve finire anche in errors.log")