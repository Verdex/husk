
import pygame

White = [255, 255, 255]

class SubWindow:
    
    def __init__(self, priority, location, screen):
        self.priority = priority 
        self.location = location
        self.screen = screen 

    def resize(self):
        # destroy screen and rebuild it with new size?
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

        self._screen.fill(White)

        for sub in self._sub_windows:
            self._screen.blit(sub.screen, sub.location)

        pygame.display.update()
