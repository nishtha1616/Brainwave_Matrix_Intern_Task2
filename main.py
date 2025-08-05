# main.py
from monitor import run_suspicious_file, start_file_monitor, monitor_process_behavior, monitor_network_connections
import threading
import time

def main():
    filepath = "dummy_malware.py"

    # Start monitors in background threads
    threading.Thread(target=start_file_monitor, args=(".",), daemon=True).start()
    threading.Thread(target=monitor_process_behavior, daemon=True).start()
    threading.Thread(target=monitor_network_connections, daemon=True).start()

    run_suspicious_file(filepath)

    # Keep the main thread alive
    while True:
        time.sleep(2)

if __name__ == "__main__":
    main()


