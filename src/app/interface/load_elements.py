from tkinter import N
from customtkinter import CTk, CTkLabel, CTkScrollableFrame, CTkOptionMenu, CTkToplevel, FontManager
from typing import Union
import pywinstyles

from app.file_view import treeview
from .file_creation import file_creation


class GUI:
    FontManager.load_font(r'src\app\interface\materials\fonts\centima.ttf')

    def __init__(self):
        self.root = CTk()
        self.root.title("RCreator - {}")
        self.root.geometry(GUI.__centralize(self, self.root))
        self.root.resizable(False, False) # Preciso criar uma configuração interna pra mudar a resolução
        self.root.config(bg="#4c4c4c")
        # self.root.bind("<Configure>", self.__on_resize)

        self.__load_elements__()
        treeview(self.file_view_label)

    def __centralize(self, Screen:Union[CTk, CTkToplevel], w=1280, h=720) -> str:
        return "{}x{}+{}+{}".format(
            w,   
            h,
            int(((Screen.winfo_screenwidth()/2) - (w/2)) * Screen._get_window_scaling()),
            int(((Screen.winfo_screenheight()/2) - (h/1.6)) * Screen._get_window_scaling())
        )        

    def __load_elements__(self):
        # bagui vai ser criar o objeto via label mesmo, pq as imagens tão com a transparencia zuada
        labels = []

        self.file_view_label = CTkLabel(self.root, fg_color="#7f7f7f", 
                                        text='File Viewer', text_color='black',
                                        anchor=N, pady=2, bg_color='#4c4c4c', 
                                        width=212, height=720, corner_radius=12,
                                        font=('centima', 14))
        
        self.workspace_label = CTkLabel(self.root, fg_color='#3a3a3a',
                                        bg_color='#2f2f2f', width=1052,
                                        height=640, corner_radius=12)
        #timeline_label = CTkLabel(self.root, fg_color='#aeaeae', bg_color='#bfbfbf', width=1035, height=36, corner_radius=8)

        self.file_view_label.place(x=0, y=0)
        self.workspace_label.place(x=228, y=81)
        #timeline_label.place(x=228, y=16)

        labels.append([self.file_view_label, self.workspace_label])
        for label_list in labels:
            for label in label_list:
                pywinstyles.set_opacity(label, color=label.cget('bg_color'))

        self.timeline = CTkScrollableFrame(self.root, width=1035, height=32, orientation='horizontal',
                                      corner_radius=8, fg_color='#aeaeae', bg_color='#4c4c4c')
        self.timeline.place(x=228, y=16)
        
        files_allowed = ['XML', 'CSHARP', 'TEXT']

        self.create_file_menu = CTkOptionMenu(self.root, width=141, height=11,
                                    button_color="#7a7a7a", button_hover_color="#8C8C8C",
                                    dropdown_fg_color="#7a7a7a", dropdown_hover_color="#8C8C8C",
                                    fg_color="#7a7a7a", bg_color="#3a3a3a", values=files_allowed,
                                    font=('centima', 14), command=lambda value: (file_creation(self.create_file_menu, 
                                                                            self.timeline, 
                                                                            value, 
                                                                            self.root,
                                                                            self.workspace_label,
                                                                            )))
        self.create_file_menu.set("Create File")
        self.create_file_menu.place(in_=self.workspace_label, x=0, y=0)

    def start(self):
        self.root.mainloop()
    
