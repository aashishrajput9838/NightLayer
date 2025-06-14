# NightLayer

NightLayer is a simple Python application that creates a semi-transparent black overlay on your laptop screen. It can be toggled on and off, and its opacity adjusted, using keyboard shortcuts or a system tray icon.

## Features

*   **Toggle Overlay:** Turn the black overlay on/off using `Ctrl + Space`.
*   **Adjust Opacity:**
    *   Increase opacity using `Ctrl + Left Arrow`.
    *   Decrease opacity using `Ctrl + Right Arrow`.
*   **System Tray Integration:** A minimal system tray icon allows you to:
    *   Dynamically "Turn On" or "Turn Off" the layer.
    *   "Close" the application permanently.
*   **Minimal Interface:** No visible main window, runs discreetly in the background.
*   **Executable:** Can be built into a standalone `.exe` file for Windows.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/aashishrajput9838/NightLayer.git
    cd NightLayer
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    This will install `keyboard`, `pywin32`, `pystray`, `Pillow`, and `pyinstaller`.

## Usage

### Running from Python Script

To run the application directly from the Python script:

```bash
python night_layer.py
```

**Note:** The application requires **administrator privileges** to register global hotkeys.

### Using the Executable

If you have built the `.exe` file (see "Building Executable" below), you can simply run `night_layer.exe` from the `dist` folder.

### Controls

*   **Toggle Overlay:** Press `Ctrl + Space`
*   **Increase Opacity:** Press `Ctrl + Left Arrow`
*   **Decrease Opacity:** Press `Ctrl + Right Arrow`
*   **System Tray Icon:** Right-click the semi-transparent grey square icon in your system tray to access "Turn On", "Turn Off", and "Close" options.
*   **Exit Application:** Press `Esc` (when the application is in focus, or during development) or use the "Close" option from the system tray menu.

## Building Executable

To create a standalone executable (`.exe`) file for Windows (8.1, 10, 11) using `PyInstaller`:

1.  **Ensure PyInstaller is installed:**
    ```bash
    pip install pyinstaller
    ```
    (It should already be installed if you followed the main installation steps).

2.  **Generate the executable:**
    ```bash
    pyinstaller --onefile --noconsole night_layer.py
    ```

The executable (`night_layer.exe`) will be located in the newly created `dist` folder. 