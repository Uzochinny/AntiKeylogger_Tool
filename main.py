import tkinter as tk
import threading
import time
import logging
import sys
from keylogger_detector import detect_keyloggers
from keylogger_blocker import block_keyloggers
from stop_tool import stop_tool

# Setup logging configuration
logging.basicConfig(filename='anti_keylogger.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Function to log detected keyloggers
def log_detection(keylogger_name):
    logging.info(f"Detected keylogger: {keylogger_name}")

class AntiKeyloggerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Anti-Keylogger Tool")
        self.master.geometry("400x300")

        # Status Label
        self.status_label = tk.Label(master, text="Status: Idle", fg="green")
        self.status_label.pack(pady=10)

        # Start and Stop Buttons
        self.start_button = tk.Button(master, text="Start Monitoring", command=self.start_monitoring)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(master, text="Stop Tool", command=self.stop_tool, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

        # Thread for monitoring keyloggers
        self.monitoring_thread = None

    def update_status(self, text, color="green"):
        """Update the status label."""
        self.status_label.config(text=f"Status: {text}", fg=color)

    def start_monitoring(self):
        """Start the monitoring thread."""
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.monitoring_thread = threading.Thread(target=self.monitor_keyloggers)
        self.monitoring_thread.daemon = True
        self.monitoring_thread.start()

    def monitor_keyloggers(self):
        """Monitor keyloggers and block them if detected."""
        while True:
            detected_keyloggers = detect_keyloggers()
            if detected_keyloggers:
                for keylogger in detected_keyloggers:
                    log_detection(keylogger['name'])
                    self.update_status(f"Keylogger Detected: {keylogger['name']}", color="red")
                    block_keyloggers([keylogger])
                    time.sleep(1)  # Delay after blocking keylogger
            time.sleep(5)  # Scan every 5 seconds

    def stop_tool(self):
        """Stop the anti-keylogger tool."""
        stop_tool()

# Run the GUI Application
if __name__ == "__main__":
    root = tk.Tk()
    gui = AntiKeyloggerGUI(root)
    root.mainloop()
