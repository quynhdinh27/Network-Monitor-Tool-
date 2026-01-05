# Network Monitor Tool (Tkinter GUI)

A simple GUI-based network monitoring application built with **Python Tkinter**.  
The tool allows users to check the status of a host by entering an **IP address or domain name**.  
It performs **ping testing**, **basic port checking**, and **logs results** for monitoring purposes.

---

## Features

- 🖥️ **Graphical User Interface** using Tkinter
- 🌐 Accepts **IP address or domain name** as input
- 📡 **Ping check** to determine host availability (OK / FAIL)
- 🔌 **Common port scanning** (e.g. 80, 443, 22, 21)
- 📊 Displays **port status** (Open / Closed)
- 📝 **Automatic logging** of results to a log file
- ⏱️ Fast and lightweight monitoring tool

---

## How It Works

1. User enters an **IP address or domain name**
2. The program performs:
   - Ping test to check connectivity
   - Scan of common ports
3. Results are:
   - Displayed on the GUI
   - Saved to a log file for later review

---

## Technologies Used

- Python 3
- Tkinter (GUI)
- `socket` (port checking)
- `subprocess` / `os` (ping command)
- File handling for logging

---

## Requirements

- Python **3.8+**
- Works on **Windows / Linux / macOS**

No external libraries are required.

---
