import win32api
import win32con
import time
import tkinter as tk
from threading import Thread
import keyboard

# Create the main application window
root = tk.Tk()
root.geometry("300x300")
root.title("F3 Macro")

# Flag to indicate whether the macro is running or not
running = False

def start_macro(event):
    global running
    if not running:
        start_button.config(text="Release F3 to Stop", state=tk.DISABLED)
        stop_button.config(state=tk.NORMAL)
        running = True
        Thread(target=press_f3).start()
        print("Macro started. Release F3 to stop.")

def stop_macro(event):
    global running
    if running:
        start_button.config(text="Press F3 to Start", state=tk.NORMAL)
        stop_button.config(state=tk.DISABLED)
        running = False
        print("Macro stopped.")

# Function to simulate the macro
def press_f3():
    # Hold down the F3 key
    win32api.keybd_event(0x72, 0, 0, 0)

    while running:
        # Press the F3 key four times with a 1-second interval
        for i in range(4):
            win32api.keybd_event(0x72, 0, 0, 0)
            time.sleep(1)
            win32api.keybd_event(0x72, 0, win32con.KEYEVENTF_KEYUP, 0)

    # Release the F3 key
    win32api.keybd_event(0x72, 0, win32con.KEYEVENTF_KEYUP, 0)

    # Update the button text and disable the "Stop" button
    start_button.config(text="Press F3 to Start", state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)
    print("Macro stopped.")

# Bind the F3 key to the start_macro and stop_macro functions
keyboard.on_press_key('f3', start_macro)
keyboard.on_release_key('f3', stop_macro)

# Create the GUI elements
start_button = tk.Button(root, text="Press F3 to Start", command=start_macro)
start_button.pack(pady=10)
stop_button = tk.Button(root, text="Stop", command=stop_macro, state=tk.DISABLED)
stop_button.pack(pady=10)

# Start the main event loop
root.mainloop()
