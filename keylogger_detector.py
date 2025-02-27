import psutil

# List of known keylogger process names (extend as necessary)
KEYLOGGER_SIGNATURES = ["keylogger.exe", "spynet.exe", "logger.exe"]

def detect_keyloggers():
    """Detects processes that match known keylogger signatures."""
    keyloggers_found = []
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'].lower() in KEYLOGGER_SIGNATURES:
            keyloggers_found.append(proc.info)
    return keyloggers_found


