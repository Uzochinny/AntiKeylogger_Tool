import tkinter as tk
from keylogger_detector import detect_keyloggers
from keylogger_blocker import block_keyloggers
from stop_tool import stop_tool
import threading
import time

class AntiKeyloggerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Anti-Keylogger Tool")
        self.master.geometry("400x300")

        self.status_label = tk.Label(master, text="Status: Idle", fg="green")
        self.status_label.pack(pady=10)

        self.start_button = tk.Button(master, text="Start Monitoring", command=self.start_monitoring)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(master, text="Stop Tool", command=self.stop_tool, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

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
                self.update_status("Keylogger Detected! Blocking...", color="red")
                block_keyloggers(detected_keyloggers)
                self.update_status("Monitoring Keyloggers...", color="green")
            time.sleep(5)

    def stop_tool(self):
        """Stop the anti-keylogger tool."""
        stop_tool()

# Running the GUI
if __name__ == "__main__":
    root = tk.Tk()
    gui = AntiKeyloggerGUI(root)
    root.mainloop()
