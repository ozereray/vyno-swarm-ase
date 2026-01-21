import logging
import os

def setup_vyno_logger(name: str = "VYNO_CORE"):
    """Configures the global logger for the swarm ecosystem."""
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        
        # Console Handler
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        logger.addHandler(ch)
    return logger

logger = setup_vyno_logger()