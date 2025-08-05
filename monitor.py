# monitor.py
import subprocess
import psutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def run_suspicious_file(filepath):
    try:
        subprocess.Popen(["python", filepath])
        print(f"[+] Running: {filepath}")
    except Exception as e:
        print(f"[!] Error running {filepath}: {e}")

# File monitor
class MonitorHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f"[Modified] {event.src_path}")
    def on_created(self, event):
        print(f"[Created] {event.src_path}")
    def on_deleted(self, event):
        print(f"[Deleted] {event.src_path}")

def start_file_monitor(path="."):
    observer = Observer()
    handler = MonitorHandler()
    observer.schedule(handler, path=path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

# CPU/Process Monitor
def monitor_process_behavior():
    while True:
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
            try:
                if proc.info['cpu_percent'] > 50:
                    print(f"[!] High CPU usage: {proc.info}")
            except:
                continue
        time.sleep(3)

# Network Monitor
def monitor_network_connections():
    while True:
        for conn in psutil.net_connections():
            if conn.status == 'ESTABLISHED' and conn.raddr:
                print(f"[!] Connection: {conn.laddr} -> {conn.raddr}")
        time.sleep(3)
