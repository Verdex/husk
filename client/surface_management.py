
import pygame
from database import Surfaces

class SingleSurface:

    def __init__(self, surface, location, size, priority):
        self.surface = surface
        self.location = location
        self.size = size
        self.priority = priority


class MainScreen:

    def __init__(self, surface, size):
        self.surface = surface
        self.size = size
    
    def update(self):
        for surface in sorted( Surfaces.all(), key=lambda s: s.priority ):
            assert type(surface) == SingleSurface
            self.surface.blit(surface.surface, surface.location)


def init_main_screen(width, height):
    best_depth = pygame.display.mode_ok((width, height), 0, 32)
    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE, best_depth) 
    main = MainScreen(screen, (width, height))
    return main
