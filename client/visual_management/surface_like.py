
import pygame

White = [255, 255, 255]

class JustSurface:
    
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


class SurfaceManager:

    def __init__(self, background):
        self.priority = 0
        self._background = background
        self._surfaces = []

    def add_surface(self, surface):
        self._surfaces.append(window)
        sorted( self._surfaces, key=lambda sub: sub.priority )

    def update(self):

        self._screen.fill(White)

        for sub in self._sub_windows:
            sub_screen = sub.update()
            self._screen.blit(sub_screen, sub.location)

        pygame.display.update()
