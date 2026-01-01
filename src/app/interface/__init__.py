import ctypes
import sys
from tkinter import messagebox
from .load_elements import GUI

def start_gui():
    if not ctypes.windll.shell32.IsUserAnAdmin():
        messagebox.showwarning("Warn", message='Not enough priviledge.\n Restarting...')
        ctypes.windll.shell32.IsUserAnAdmin(
            None, 'runas', sys.executable, ' '.join(sys.argv), None, None
        )
    else:
        GUI().start()

    