
import pygame

White = [255, 255, 255]

class SubWindow:
    
    def __init__(self, priority, location, size):
        self.priority = priority 
        self.location = location
        self.size = size
        self._screen = pygame.Surface(size) 

    def resize(self, size):
        self._screen = pygame.Surface(size)
        self.size = size

    def move(self, location):
        self.location = location
    
    def render(self, updater):
        updater(self._screen)

    def update(self, updater):
        return self._screen


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
            sub_screen = sub.update()
            self._screen.blit(sub_screen, sub.location)

        pygame.display.update()
