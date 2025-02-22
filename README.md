# ExScript Aimbot

ExScript Aimbot is a **Python-based aimbot** designed for educational purposes. It uses **YOLOv11** for object detection and **PyAutoGUI** for mouse control. The script includes a **futuristic GUI** built with `customtkinter`, key validation, and support for both **Aimbot** and **Triggerbot** modes.

---

## Features

- **Key Validation**: Validates user keys against a remote list.
- **Aimbot/Triggerbot Modes**:
  - **Aimbot**: Moves the cursor to the target and shoots.
  - **Triggerbot**: Shoots instantly when the cursor is near the target.
- **CS2 Process Checking**: Waits for `cs2.exe` to start before running.
- **Futuristic GUI**: Built with `customtkinter` for a modern look.
- **Loading Screen**: Displays a loading screen after key validation.

---

## Requirements

- Python 3.8+
- Libraries:
  - `ultralytics` (for YOLOv11)
  - `customtkinter` (for GUI)
  - `pyautogui` (for mouse control)
  - `mss` (for screen capture)
  - `psutil` (for process checking)
  - `Pillow` (for image processing)
  - `requests` (for fetching keys)

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/exscript-aimbot.git
   cd exscript-aimbot
   python wow.py
   ```
