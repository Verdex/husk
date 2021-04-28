
import pygame

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
        if id.value in self.surfaces:
            del self.surfaces[id.value]

    def update(self):
        for surface in sorted( self.surfaces.values(), key=lambda s: s.priority ):
            if type(surface) == AggregateSurface: 
                surface.update()
            elif type(surface) == SingleSurface:
                self.surface.blit(surface.surface, surface.location)
            else:
                raise SystemError(f"Encountered unknown surface type: {type(surface)}")

def create_game_surface(database, main_screen, size):
    assert type(main_screen) == AggregateSurface
    s = SingleSurface(pygame.Surface(size), (0, 0), size, 0)
    database.add(s)
    main_screen.add(s)
    return s

def resize_game_surface(surface, database, main_screen, size):
    assert type(surface) == SingleSurface
    database.remove(surface.id)
    main_screen.remove(surface.id)
    return create_game_surface(database, main_screen, size)

def init_main_screen(database, width, height):
    best_depth = pygame.display.mode_ok((width, height), 0, 32)
    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE, best_depth) 
    main = AggregateSurface(screen, (0, 0), (width, height), 0)
    database.add(main)
    return main
