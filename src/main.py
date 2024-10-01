import tkinter as tk
from tkinter import Canvas
from PIL import Image, ImageTk
import win32gui
import win32con
import keyboard
import configparser


def read_config():
    """Reads and returns configuration values from a config file."""
    config = configparser.ConfigParser()
    config.read("config.ini")

    # Access values from the configuration file
    transparency = config.get("General", "transparency", fallback=0.5)
    hotkey = config.get("General", "hotkey", fallback="ctrl+alt+f12")
    image_path = config.get(
        "File", "image_path", fallback="img\\photo_2024-09-21_18-04-12.jpg"
    )

    return {"transparency": transparency, "image_path": image_path, "hotkey": hotkey}


def set_clickthrough(hwnd):
    """Set the window to be clickthrough (transparent to mouse clicks)."""
    try:
        styles = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
        styles |= win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, styles)
        win32gui.SetLayeredWindowAttributes(hwnd, 0, 255, win32con.LWA_ALPHA)
    except Exception as e:
        print(f"Error setting clickthrough: {e}")


def size_position_for_picture(root, bg, img_id, sw, sh):
    """Resize and reposition the window based on image size."""
    bbox = bg.bbox(img_id)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x, y = sw // 2 - w // 2, sh // 2 - h // 2
    root.geometry(f"{w}x{h}+{x}+{y}")
    bg.configure(width=w, height=h)


def close_window(root):
    """Closes the Tkinter window."""
    root.destroy()


def setup_window(image_path, transparency, hotkey):
    """Sets up the Tkinter window and displays the image."""
    # Initialize Tkinter window
    root = tk.Tk()
    root.overrideredirect(1)  # Remove window decorations
    root.attributes("-alpha", transparency)
    root.attributes("-transparentcolor", "white", "-topmost", 1)

    # Create a canvas with a white background
    bg = Canvas(root, bg="white", highlightthickness=0)
    root.config(bg="white")

    # Load and display image
    frame = ImageTk.PhotoImage(file=image_path)
    img_id = bg.create_image(0, 0, image=frame, anchor="nw")
    bg.pack()

    # Get screen dimensions
    sw, sh = root.winfo_screenwidth(), root.winfo_screenheight()

    # Set window size and position based on the image
    size_position_for_picture(root, bg, img_id, sw, sh)

    # Set clickthrough state
    set_clickthrough(bg.winfo_id())

    # Set global hotkey to close the window with Ctrl+Alt+F12
    keyboard.add_hotkey(hotkey, lambda: close_window(root))

    # Start the Tkinter mainloop
    root.mainloop()


if __name__ == "__main__":
    # Read configuration
    config = read_config()

    # Set up the window and run the app
    setup_window(config["image_path"], config["transparency"], config["hotkey"])
