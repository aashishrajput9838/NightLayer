# NightLayer 🌙

NightLayer is a sleek Python application that creates a semi-transparent black overlay on your laptop screen for comfortable night-time viewing. It can be toggled on and off, and its opacity adjusted, using keyboard shortcuts or a system tray icon.

## ✨ Features

*   **Toggle Overlay:** Turn the black overlay on/off using `Ctrl + Space`.
*   **Adjust Opacity:** 
    *   Make screen brighter using `Ctrl + Up Arrow` (decreases overlay opacity).
    *   Make screen darker using `Ctrl + Down Arrow` (increases overlay opacity).
*   **Status Indicator:** Shows "Night Layer Active" in the top-left corner when the overlay is enabled.
*   **System Tray Integration:** A minimal system tray icon allows you to:
    *   Dynamically "Turn On" or "Turn Off" the layer.
    *   "Close" the application permanently.
*   **Minimal Interface:** No visible main window, runs discreetly in the background.
*   **Executable:** Can be built into a standalone `.exe` file for Windows.

## 🚀 Installation

### Method 1: Direct Download (Easiest) 📥

1. **Download the ZIP file:**
   - Go to [NightLayer GitHub](https://github.com/aashishrajput9838/NightLayer)
   - Click the green "Code" button
   - Select "Download ZIP"
   - Extract the ZIP file to your desired folder

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Method 2: Git Users (If you know git) 🔧

```bash
git clone https://github.com/aashishrajput9838/NightLayer.git
cd NightLayer
pip install -r requirements.txt
```

## 🎮 Usage

### Running from Python Script

To run the application directly from the Python script:

```bash
python night_layer.py
```

**Note:** The application requires **administrator privileges** to register global hotkeys.

### Using the Executable

If you have built the `.exe` file (see "Building Executable" below), you can simply run `night_layer.exe` from the `dist` folder.

### 🎯 Controls

*   **Toggle Overlay:** Press `Ctrl + Space`
*   **Make Brighter:** Press `Ctrl + Up Arrow` (decreases overlay opacity)
*   **Make Darker:** Press `Ctrl + Down Arrow` (increases overlay opacity)
*   **Exit Application:** Press `Ctrl + Shift + C`
*   **System Tray Icon:** Right-click the semi-transparent grey square icon in your system tray to access "Turn On", "Turn Off", and "Close" options.

### 📍 Status Indicator

When the night layer is active, you'll see a subtle "Night Layer Active" text in the top-left corner of your screen. This indicator is barely visible and won't interfere with your work, but confirms that the overlay is enabled.

## 🔧 Building Executable

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

## 🎨 How It Works

NightLayer creates a fullscreen, transparent black window that sits on top of all other applications. By adjusting the opacity of this overlay, you can control how much light reaches your eyes:

- **Lower opacity** = More light passes through = Brighter screen
- **Higher opacity** = Less light passes through = Darker screen

The overlay is completely non-intrusive and allows you to continue using all your applications normally while protecting your eyes from bright screen light.

## 🔄 Recent Updates

### Version 2.0.0 (Latest) 🚀
- ✅ Fixed hotkey compatibility issues
- ✅ Added status indicator for active state
- ✅ Improved intuitive controls (Up = brighter, Down = darker)
- ✅ Enhanced system tray integration
- ✅ Optimized performance and stability

**Download Latest Version:** [NightLayer_v2.0.exe](https://github.com/aashishrajput9838/NightLayer/releases)

See [CHANGELOG.md](CHANGELOG.md) for detailed version history.

## 📝 Requirements

- Windows 8.1, 10, or 11
- Python 3.7+
- Administrator privileges (for global hotkeys)

## 🤝 Contributing

Feel free to submit issues and enhancement requests! 