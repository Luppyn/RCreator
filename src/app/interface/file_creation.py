from tkinter import BOTH, CENTER, W
from tkinter.ttk import Treeview
from customtkinter import CTkEntry, CTkButton, CTkImage, CTkOptionMenu, CTkScrollableFrame, CTk, CTkLabel
import PIL.Image
from ..ide import ide_implement



def file_creation(create_file_menu:CTkOptionMenu, timeline:CTkScrollableFrame, value:str, root:CTk, workspace_label:CTkLabel, **kw):
    def __icon_set(type:str):
        return CTkImage(PIL.Image.open(fr"src\app\interface\materials\imgs\{type.lower()}-icon.png"))

    def __name_file(new_file):
        def __finish_rename():
            file_name_value = file_name.get()

            if file_name_value != "":
                new_file.configure(text=file_name.get())

            create_file_menu.configure(state="normal")
            new_file.configure(state='normal')
            file_name.destroy()

        def __cancel_rename():
            create_file_menu.configure(state='normal')
            new_file.configure(state='normal')
            file_name.destroy()

        new_file.configure(state="disabled")
        create_file_menu.configure(state="disabled")

        file_name = CTkEntry(workspace_label, width=100, height=16, border_width=0,
                             fg_color="#7B7B7B", font=('centima', 14))
        file_name.place(x=145, y=0)
        file_name.focus_force()

        workspace_label.bind('<Button-1>', lambda event: __finish_rename())
        file_name.bind('<Return>', lambda event: __finish_rename())
        file_name.bind('<FocusOut>', lambda event: __finish_rename())
        file_name.bind('<Escape>', lambda event: __cancel_rename())


    create_file_menu.set('Create File')
    new_file = CTkButton(timeline, image=__icon_set(lang:=value), width=77, 
                            height=26, text=value, fg_color="#7B7B7B", 
                            hover_color="#595959", font=('centima', 16))
    new_file.pack(ipadx=4, padx=4, side='right')
    
    ide_implement(workspace_label, lang) # chamar apenas quando alterar o arquivo
    new_file.bind('<Double-Button-1>', lambda event: __name_file(new_file))