
from surface_management import SingleSurface
import pygame

White = [255, 255, 255]
Black = [0, 0, 0]

TextHeight = 15
HorizontalMargin = 10
EntryLineOffset = 18

class Console:

    def __init__(self, surface):
        self.active = False
        self.surface = surface
        self.entry = []
        self.history = []

    def update_surface(self):
        draw(self.surface, self.entry, self.history)
    

def draw_box(surface):
    pygame.draw.line( surface.surface \
                    , Black \
                    , (0, 0) \
                    , (surface.size[0], 0))

    pygame.draw.line( surface.surface \
                    , Black \
                    , (0, 0) \
                    , (0, surface.size[1]))

    pygame.draw.line( surface.surface \
                    , Black \
                    , (surface.size[0] - 1, 0) \
                    , (surface.size[0] - 1, surface.size[1] - 1) ) 

    pygame.draw.line( surface.surface \
                    , Black \
                    , (0, surface.size[1] - 1) \
                    , (surface.size[0] - 1, surface.size[1] -1) )

def draw_entry_line(surface):
    pygame.draw.line( surface.surface \
                    , Black \
                    , (0, surface.size[1] - EntryLineOffset) \
                    , (surface.size[0], surface.size[1] - EntryLineOffset))

def draw_text(font, text, location, surface):
    text_surface = font.render(text, True, Black)
    surface.blit(text_surface, location)

def draw(surface, char_list, history):
    surface.surface.fill(White)
    draw_box(surface)
    draw_entry_line(surface)

    font = pygame.font.SysFont(None, 18)

    entry = ''.join(char_list)

    draw_text(font, entry, (HorizontalMargin, surface.size[1] - TextHeight), surface.surface)

    offset = 2
    for h in history:
        draw_text(font, h, (HorizontalMargin, surface.size[1] - (TextHeight * offset)), surface.surface)
        offset += 1


def init_console(database, main_screen):
    s = SingleSurface(pygame.Surface((200, 200)), (10, 10), (200, 200), 0)
    database.add(s)
    main_screen.add(s)
    return Console(s)
