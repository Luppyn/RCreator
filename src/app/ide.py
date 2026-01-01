from tkinter import messagebox
from cupcake import Editor, Languages
from customtkinter import CTkLabel, CTkButton
import pythonnet
import platform

def __run_on_os__():
    if bool(platform.platform().lower().find('windows')):
        try:
         return pythonnet.set_runtime('mono')
        except RuntimeError as exc:
            messagebox.showerror('Error', message=f'{exc}\n Please, try to run on windows.') # Preciso testar no linux
            quit()

def ide_implement(workspace:CTkLabel, lang:str):
    width = workspace.winfo_width()
    height = workspace.winfo_height()

    ide = Editor(workspace, language=getattr(Languages, lang), width=width, height=height)
    ide.place(in_=workspace, y=20, x=0, width=width, height=height-20)

    # run
    def run():
        __run_on_os__()
        run_button.configure(state='disabled')
        code = str(ide.content.get("1.0", "end-1c")) # type: ignore
        try:
            pythonnet.load(params=code) # Só funciona em versão python 3.7-3.13 | a minha é 3.14 😭
        except Exception as exc:
            messagebox.showerror('Error', message=exc) # pyright: ignore[reportArgumentType]
            exec(code) # type: ignore

        run_button.configure(state='normal')

    run_button = CTkButton(workspace, width=100, height=16, text='Run', command=run)
    run_button.place(x=width-100, y=0)
