# NightLayer 🌙

<p align="center">
  <img src="https://img.shields.io/badge/OS-Windows-blue?style=for-the-badge&logo=windows" alt="Windows Support">
  <img src="https://img.shields.io/badge/Language-Python-yellow?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/github/v/release/aashishrajput9838/NightLayer?style=for-the-badge&color=green" alt="Latest Release">
</p>

---

### **Overview**
**NightLayer** is a sophisticated Windows utility designed to reduce eye strain by creating a customizable, semi-transparent black overlay across your entire screen. It allows you to dim your display beyond hardware limitations, perfect for late-night sessions or sensitive eyes.

---

## 📥 **Quick Start**

**No installation required!**
1. **[Download NightLayer_v2.0.exe](https://github.com/aashishrajput9838/NightLayer/releases)**
2. Run the file.
3. Enjoy a more comfortable viewing experience.

*Works seamlessly on Windows 8.1, 10, and 11.*

---

## ✨ **Key Features**

- 🌗 **Instant Toggle**: Quickly enable or disable the overlay with a global shortcut.
- 🎚️ **Dynamic Opacity**: Fine-tune your screen's darkness using intuitive keyboard controls.
- 🛰️ **Subtle Indicator**: A minimal "Night Layer Active" status in the corner keeps you informed.
- 📦 **Tray Management**: Control everything from a sleek system tray icon.
- 🚀 **Zero Footprint**: Runs discreetly in the background with minimal resource usage.
- 🛠️ **Standalone**: Portable executable with no dependencies needed.

---

## 🎮 **Controls & Usage**

| Action | Shortcut |
| :--- | :--- |
| **Toggle Overlay** | `Ctrl + Space` |
| **Increase Brightness** | `Ctrl + Up Arrow` |
| **Increase Darkness** | `Ctrl + Down Arrow` |
| **Exit Application** | `Ctrl + Shift + C` |

> [!TIP]
> **Administrator Privileges**: To ensure global hotkeys work correctly across all applications, please run NightLayer as an Administrator.

---

## 🔧 **Installation for Developers**

If you prefer to run from source or contribute:

### **1. Clone & Setup**
```bash
git clone https://github.com/aashishrajput9838/NightLayer.git
cd NightLayer
```

### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3. Run**
```bash
python night_layer.py
```

---

## 🏗 **Building Your Own EXE**

Want to package it yourself? We use `PyInstaller`:

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole night_layer.py
```
Your standalone executable will be generated in the `dist/` directory.

---

## 🎨 **Technical Concept**

NightLayer operates by creating a fullscreen, undecorated Tkinter window set to `-topmost`. It utilizes the Windows `alpha` attribute to adjust transparency:
- **Low Alpha**: High transparency, brighter screen.
- **High Alpha**: Low transparency, darker screen.

---

## 🔄 **Recent Updates**

### **Version 2.0.0** 🚀
- ✨ Added subtle active-state status indicator.
- ⌨️ Refined hotkey responsiveness.
- 🛠 Improved system tray menu with dynamic toggles.
- 📈 Performance optimizations for low CPU usage.

Check the [CHANGELOG.md](CHANGELOG.md) for a full history of changes.

---

## 🤝 **Contributing**

Contributions are welcome! If you have ideas for features or find bugs, please:
1. Fork the repository.
2. Create a feature branch.
3. Submit a Pull Request.

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/aashishrajput9838">Aashish Rajput</a>
</p>
