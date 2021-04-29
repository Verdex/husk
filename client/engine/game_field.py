
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
        self.surface_id = create_game_surface(size)

    def resize(self, size):
        self.surface_id = resize_game_surface( self.surface_id, size )

    def update(self):
        surface = Surfaces.get(self.surface_id)
        surface.surface.fill(color.White)
        for mob_surface in MobFieldObjects.all():
            mob_surface.renderer.render(surface, mob_surface.location)

def create_game_surface(size):
    s = SingleSurface(pygame.Surface(size), (0, 0), size, 0)
    id = Surfaces.add(s)
    return id 

def resize_game_surface(surface_id, size):
    Surfaces.remove(surface_id)
    return create_game_surface(size)