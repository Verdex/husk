
class SubWindow:
    
    def __init__(self):
        self.priority = 0
        self.location = (0, 0)

    def resize(self):
        pass

    def move(self):
        pass
    
    def update(self):
        pass


class WindowManager:

    def __init__(self, screen):
        self._screen = screen
        self._sub_windows = []

    def add_sub_window(self, window):
        self._sub_windows.append(window)
        sorted( self._sub_windows, key=lambda sub: sub.priority )

    def update(self):
        pass
