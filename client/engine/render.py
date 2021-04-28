
from engine.resources import AtSymbolId
import color

import pygame

class AtSymbolRenderer:
    def __init__(self):
        font = pygame.font.SysFont(None, 18)
        self.text_surface = font.render("@", True, color.Black)

    def render(self, surface, location):
        surface.surface.blit(self.text_surface, location)


Renderers = { AtSymbolId.value: AtSymbolRenderer() \
            }
