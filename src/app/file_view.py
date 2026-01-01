import os
from tkinter.ttk import Style, Treeview
from app.interface.load_path import load_path
from app.update_file import FolderChangeHandler
from watchdog.observers import Observer

def start_watcher(tree, root, path):
    def refresh():
        treeview(tree)

    handler = FolderChangeHandler(root, refresh)
    observer = Observer()
    observer.schedule(handler, path, recursive=True)
    observer.daemon = True
    observer.start()

def treeview(file_view):
    Treeview().destroy()
    def __get_file_type__(filename):
        _, ext = os.path.splitext(filename)
        return ext[1:].upper() if ext else ""

    width = file_view.winfo_width()
    height = file_view.winfo_height()

    #style
    style = Style()
    style.theme_use("default")
    
    style.configure(
        "Custom.Treeview",
        background="#7f7f7f",
        foreground="#1e1e1e",
        fieldbackground="#7f7f7f",
        rowheight=22,
        font=('centima', 10)
    )

    style.map(
        "Custom.Treeview",
        background=[('selected', "#3D3D3D")],
    )


    #treeview
    work_path = load_path() # type: ignore
    folder_name = os.path.basename(work_path) # type: ignore

    file_tree = Treeview(file_view,
                         style="Custom.Treeview",
                         columns=('name','path'),
                         show='tree headings')
    
    file_tree.heading('#0', text=folder_name) # pasta pai
    file_tree.heading('#1', text='Type')

    work_item = file_tree.insert("", "end", text=folder_name, open=True)

    for item in os.listdir(work_path):
        full_path = os.path.join(work_path, item) # type: ignore

        if os.path.isdir(full_path):
            folder_id = file_tree.insert(
                                work_item,
                                'end',
                                text=item,
                                values=('',),
                                open=False
                            )
            
            for sub in os.listdir(full_path):
                sub_path = os.path.join(full_path, sub)
                if os.path.isfile(sub_path):
                    file_tree.insert(
                        folder_id,
                        'end',
                        text=sub,
                        values=(__get_file_type__(sub),)
                    )
        
        else:
            file_tree.insert(
                work_item,
                'end',  
                text=item,
                values=(__get_file_type__(item),)
            )


    file_tree.tag_configure('foreground', foreground="#7f7f7f")
    file_tree.place(in_=file_view, y=20, x=0, width=width, height=height)

    start_watcher(file_tree, file_view, work_path)   
    