# Brainwave_Matrix_Intern_Task2
# 🛡️ Malware Detection Sandbox (Python)

A simple sandbox environment to detect and monitor malware-like behavior using Python. This tool executes suspicious files in isolation and observes system behaviors such as process activity, file system changes, and network connections.

---

## 🚀 Features

- ✅ Execute suspicious Python files safely
- 📁 Monitor file system changes in real-time
- 🔍 Detect high CPU usage processes
- 🌐 Observe active network connections
- 📄 Console-based logging for behavioral analysis

---

## 📂 Project Structure
malware_sandbox/
├── main.py # Entry point to run the sandbox
├── monitor.py # Contains monitoring and execution logic
├── dummy_malware.py # Simulated malware script for testing
├── requirements.txt # Dependencies
└── README.md # You're reading it!

---

## 📦 Requirements

- Python 3.7+
- Packages:
  - `psutil`
  - `watchdog`

Install all dependencies with:

```bash
pip install -r requirements.txt

