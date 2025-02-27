import logging

def setup_logging():
    """Setup the logging configuration."""
    logging.basicConfig(filename='anti_keylogger.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

def log_detection(keylogger_name):
    """Log detected keylogger event."""
    logging.info(f"Detected keylogger: {keylogger_name}")
