
from surface_management import SingleSurface
from database import Surfaces, MobFieldObjects 
import color
import pygame

class FieldObject:
    def __init__(self, location, renderer):
        self.location = location
        self.renderer = renderer

class Field:

    def __init__(self, size):
        self.single_surface = create_game_surface(size)

    def resize(self, size):
        self.single_surface = resize_game_surface( self.single_surface, size )

    def update(self):
        self.single_surface.surface.fill(color.White)
        for mob_surface in MobFieldObjects.all():
            mob_surface.renderer.render(self.single_surface, mob_surface.location)

def create_game_surface(size):
    s = SingleSurface(pygame.Surface(size), (0, 0), size, 0)
    Surfaces.add(s)
    return s

def resize_game_surface(surface, size):
    assert type(surface) == SingleSurface
    Surfaces.remove(surface.id)
    return create_game_surface(size)