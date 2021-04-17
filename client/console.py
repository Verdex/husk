
from surface_management import SingleSurface
import pygame

ConsolePriority = 1

White = [255, 255, 255]
Black = [0, 0, 0]

TextHeight = 15
HorizontalMargin = 10
EntryLineOffset = 18

class Console:

    def __init__(self, surface, database, main_screen):
        self.active = False
        self.surface = surface
        self.database = database
        self.main_screen = main_screen
        self.entry = []
        self.history = []
        self.commands = { "resize": lambda x, sep: x.resize(sep) \
                        , "move" : lambda x, sep: x.move(sep) \
                        }

    def update_surface(self):
        self.surface.surface.fill(White)
        if self.active:
            draw(self.surface, self.entry, self.history)
    
    def process_key(self, event):
        if event.key == pygame.K_RETURN:
            text = ''.join(self.entry)
            if len(self.history) > 100:
                self.history.pop()
            self.history.insert(0, text)
            self.entry = []
            sep = [ s for s in text.split(' ') if s != '' ]
            if len(sep) > 0 and sep[0] in self.commands:
                self.commands[sep[0]](self, sep)

        elif event.key == pygame.K_BACKSPACE:
            if len(self.entry) > 0:
                self.entry.pop()
        elif event.key == pygame.K_ESCAPE:
            self.active = False
        elif event.unicode:
            self.entry.append(event.unicode)

    def resize(self, sep):
        size = (int(sep[1]), int(sep[2]))
        self.database.remove(self.surface.id)
        self.main_screen.remove(self.surface.id)
        s = SingleSurface(pygame.Surface(size), self.surface.location, size, ConsolePriority)
        self.database.add(s)
        self.main_screen.add(s)
        self.surface = s
    
    def move(self, sep):
        location = (int(sep[1]), int(sep[2]))
        self.surface.location = location

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
    s = SingleSurface(pygame.Surface((200, 200)), (10, 10), (200, 200), ConsolePriority)
    database.add(s)
    main_screen.add(s)
    return Console(s, database, main_screen)
