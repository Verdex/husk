
import pygame
from database import LocalId

class SingleSurface:

    def __init__(self, surface, location, size, priority):
        self.surface = surface
        self.location = location
        self.size = size
        self.priority = priority


class AggregateSurface:

    def __init__(self, surface, location, size, priority):
        self.surface = surface
        self.location = location
        self.size = size
        self.priority = priority
        self.surfaces = {} 
    
    def add(self, surface):
        self.surfaces[surface.id.value] = surface
    
    def remove(self, id):
        if self.surfaces[id.value]:
            del self.surfaces[id.value]

    def update(self):
        for surface in sorted( self.surfaces.values(), key=lambda s: s.priority ):
            if type(surface) == AggregateSurface: 
                surface.update()
            elif type(surface) == SingleSurface:
                self.surface.blit(surface.surface, surface.location)
            else:
                raise SystemError(f"Encountered unknown surface type: {type(surface)}")

def init_main_screen(database, width, height):
    best_depth = pygame.display.mode_ok((width, height), 0, 32)
    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE, best_depth) 
    main = AggregateSurface(screen, (0, 0), (width, height), 0)
    database.add(main)
    return main
