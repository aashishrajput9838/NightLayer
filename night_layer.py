import tkinter as tk
from tkinter import ttk
import keyboard
import win32gui
import win32con
import sys
from pystray import Icon as PyTrayIcon, Menu as PyTrayMenu, MenuItem as PyTrayMenuItem
from PIL import Image
import threading
from PIL import ImageDraw

class NightLayer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw() # Hide the main Tkinter window
        self.root.title("Night Layer")
        
        # Make the window fullscreen and transparent
        self.root.attributes('-fullscreen', True)
        self.opacity = 0.5  # Initial opacity
        self.root.attributes('-alpha', self.opacity)
        self.root.configure(bg='black')
        
        # Make window stay on top
        self.root.attributes('-topmost', True)
        
        # Remove window decorations
        self.root.overrideredirect(True)
        
        # Initially hide the window
        self.root.withdraw()
        
        # Track window state
        self.is_visible = False

        # Set up the hotkeys
        keyboard.add_hotkey('ctrl+space', self.toggle_layer)
        keyboard.add_hotkey('ctrl+left', self.increase_opacity)
        keyboard.add_hotkey('ctrl+right', self.decrease_opacity)
        
        # Bind Escape key to exit - mainly for development/testing
        self.root.bind('<Escape>', lambda e: self.exit_app())

        # Set up system tray icon
        self.create_tray_icon()
        
    def create_tray_icon(self):
        # Create a transparent image
        image = Image.new('RGBA', (64, 64), (0, 0, 0, 0)) # Fully transparent background
        draw = ImageDraw.Draw(image)
        # Draw a semi-transparent grey square in the center
        # RGB (128,128,128) is grey. Alpha (128) is 50% opaque.
        draw.rectangle((8, 8, 56, 56), fill=(128, 128, 128, 128))

        self.icon = PyTrayIcon("NightLayer", image, "Night Layer", None)
        self.update_tray_menu()
        self.icon.run_detached() # Run in a separate thread

    def turn_on_layer(self, icon, item):
        if not self.is_visible:
            self.toggle_layer()
        self.update_tray_menu()

    def turn_off_layer(self, icon, item):
        if self.is_visible:
            self.toggle_layer()
        self.update_tray_menu()

    def get_dynamic_toggle_item(self):
        if self.is_visible:
            return PyTrayMenuItem('Turn Off', self.turn_off_layer)
        else:
            return PyTrayMenuItem('Turn On', self.turn_on_layer)

    def update_tray_menu(self):
        # This method forces the tray icon menu to redraw with updated items
        self.icon.menu = PyTrayMenu(
            self.get_dynamic_toggle_item(),
            PyTrayMenuItem('Close', self.exit_app)
        )

    def toggle_layer(self):
        if self.is_visible:
            self.root.withdraw()
        else:
            self.root.deiconify()
        self.is_visible = not self.is_visible
        self.update_tray_menu()
        
    def increase_opacity(self):
        if self.is_visible:
            self.opacity = min(1.0, self.opacity + 0.1)
            self.root.attributes('-alpha', self.opacity)
        
    def decrease_opacity(self):
        if self.is_visible:
            self.opacity = max(0.1, self.opacity - 0.1)
            self.root.attributes('-alpha', self.opacity)
            
    def exit_app(self, *args):
        if hasattr(self, 'icon'):
            self.icon.stop()
        self.root.quit()
        sys.exit()
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = NightLayer()
    app.run() 