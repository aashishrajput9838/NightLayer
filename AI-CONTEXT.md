# AI Context - NightLayer 🌙

This document provides a high-level overview of the NightLayer project to help AI agents understand the codebase quickly and efficiently.

## 📌 Project Overview
**NightLayer** is a lightweight Windows utility built with Python that creates a semi-transparent black overlay across the entire screen. It serves as a software-based "night mode" or screen dimmer, allowing users to reduce screen brightness beyond hardware limits and adjust it dynamically using global hotkeys.

## 🛠 Tech Stack
- **Language:** Python 3.x
- **GUI Framework:** `tkinter` (used for the transparent overlay and status label)
- **Global Hotkeys:** `keyboard` (for system-wide shortcut listening)
- **System Tray:** `pystray` & `Pillow` (for background operation and icon management)
- **Windows Integration:** `pywin32` (imports present for potential Win32 API extensions)
- **Packaging:** `PyInstaller` (used to build standalone `.exe` files)

## 🏗 Project Structure
- `night_layer.py`: The main entry point containing the `NightLayer` class. It manages the Tkinter root, hotkey registrations, tray icon, and opacity logic.
- `requirements.txt`: Lists all Python dependencies (`keyboard`, `pywin32`, `pystray`, `Pillow`, `pyinstaller`).
- `night_layer.spec`: Configuration for PyInstaller to build the single-file executable.
- `README.md`: User-facing documentation with installation and usage instructions.
- `CHANGELOG.md`: Version history and updates.
- `dist/`: Contains the compiled `NightLayer_v2.0.exe`.
- `build/`: Temporary build artifacts from PyInstaller.

## 🚀 Core Functionality
1. **Transparent Overlay:** Creates a fullscreen, topmost, undecorated Tkinter window with a black background and variable alpha (opacity).
2. **Global Hotkeys:** Listens for specific key combinations even when the app is not in focus:
   - `Ctrl + Space`: Toggle overlay visibility.
   - `Ctrl + Up Arrow`: Decrease opacity (make screen brighter).
   - `Ctrl + Down Arrow`: Increase opacity (make screen darker).
   - `Ctrl + Shift + C`: Exit the application.
3. **System Tray Integration:** Runs in the background with a tray icon. Right-clicking provides options to turn the layer on/off or close the app.
4. **Status Indicator:** A subtle "Night Layer Active" label in the top-left corner confirms when the layer is active.

## 🛠 Development & Build
- **Running locally:** `python night_layer.py` (Requires Administrator privileges for global hotkeys).
- **Building EXE:** `pyinstaller --onefile --noconsole night_layer.py`.

## 💡 Key Implementation Details
- The main window is hidden initially using `root.withdraw()`.
- `root.attributes('-alpha', value)` is used for smooth opacity transitions.
- `root.attributes('-topmost', True)` ensures the overlay stays above all other windows.
- `root.overrideredirect(True)` removes the title bar and borders.
- The tray icon runs in a detached thread using `icon.run_detached()`.

---
*This file is intended for AI agents. For user documentation, see [README.md](file:///c:/github%202/nightlayer/NightLayer/README.md).*
