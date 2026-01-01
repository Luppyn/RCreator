import json
import os
from tkinter import messagebox
from tkinter.filedialog import askdirectory

def load_path():
    try:
        with open('settings.json', 'r+') as config:
            dict_path = config.readline().strip() # type: ignore
            if dict_path != "":
                return json.loads(dict_path)['path']
            else:
                config.close()

    except FileNotFoundError:
            
            current_path = os.getcwd()
            change_path = not messagebox.askyesno('Question', f"The path {current_path}, is where you want to work?", icon='question')

            if change_path is True:
                work_path = {'path': askdirectory()}
            else:
                work_path = {'path': current_path}

            with open('settings.json', 'w+') as config:
                config.write(json.dumps(work_path))
                config.close()

            return work_path['path']