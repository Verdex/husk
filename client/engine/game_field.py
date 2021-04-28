
from surface_management import AggregateSurface, SingleSurface
import color
import pygame

class Field:

    def __init__(self, database, main_screen, size):
        self.database = database
        self.main_screen = main_screen
        self.single_surface = create_game_surface(database, main_screen, size)

    def resize(self, size):
        self.single_surface = resize_game_surface( self.single_surface \
                                                 , self.database \
                                                 , self.main_screen \
                                                 , size )

    def update(self):
        self.single_surface.surface.fill(color.White)

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