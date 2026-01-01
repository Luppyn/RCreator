from watchdog.events import FileSystemEventHandler

class FolderChangeHandler(FileSystemEventHandler):
    def __init__(self, root_widget, callback):
        self.root = root_widget
        self.callback = callback
        self._job = None

    def on_any_event(self, event):
        if self._job:
            self.root.after_cancel(self._job)

        self._job = self.root.after(300, self.callback)