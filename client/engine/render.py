
from engine.resources import AtSymbolId

import pygame

Black = [0, 0, 0]

class AtSymbolRenderer:
    def __init__(self):
        font = pygame.font.SysFont(None, 18)
        self.text_surface = font.render("@", True, Black)

    def render(self, surface, location):
        surface.blit(self.text_surface, location)


Renderers = { AtSymbolId.value: AtSymbolRenderer() \
            }
