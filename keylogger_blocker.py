import psutil

def block_keyloggers(keyloggers):
    """Terminate keylogger processes if detected."""
    for keylogger in keyloggers:
        pid = keylogger['pid']
        try:
            proc = psutil.Process(pid)
            proc.terminate()
            print(f"Blocked keylogger: {keylogger['name']} (PID: {pid})")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            print(f"Unable to block process {keylogger['name']} (PID: {pid})")
