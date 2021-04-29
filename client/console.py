
from database import Surfaces
from surface_management import SingleSurface
from engine.resources import ResourceId
import color
import pygame

ConsolePriority = 1


TextHeight = 15
HorizontalMargin = 10
EntryLineOffset = 18

class Console:

    def __init__(self, surface, engine_manager):
        self.active = False
        self.surface = surface
        self.engine_manager = engine_manager
        self.entry = []
        self.history = []
        self.commands = { "resize": lambda x, sep: resize(x, sep) \
                        , "move" : lambda x, sep: move(x, sep) \
                        , "quit" : lambda x, sep: close_program(x, sep) \
                        , "spawn" : lambda x, sep: spawn_id(x, sep) \
                        , "despawn" : lambda x, sep: despawn_id(x, sep) \
                        }

    def update_surface(self):
        self.surface.surface.fill(color.White)
        if self.active:
            draw(self.surface, self.entry, self.history)
    
    def process_key(self, event):
        if event.key == pygame.K_RETURN:
            text = ''.join(self.entry)
            limit_append(self.history, text)
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

def despawn_id(self, sep):
    pass

def spawn_id(self, sep):
    input = convert_to_int(3, sep[1:])
    if not input:
        limit_append(self.history, "Usage: spawn <id> <X> <Y>")
        return
    result = self.engine_manager.spawn(ResourceId(input[0]), (input[1], input[2]))
    if result:
        limit_append(self.history, f"spawned with id {result.value}")
    else:
        limit_append(self.history, "spawn failed")

def close_program(self, sep):
    self.engine_manager.active = False

def resize(self, sep):
    input = convert_to_int(2, sep[1:])
    if not input:
        limit_append(self.history, "Usage: resize <width> <height>")
        return
    size = (input[0], input[1])
    Surfaces.remove(self.surface.id)
    s = SingleSurface(pygame.Surface(size), self.surface.location, size, ConsolePriority)
    Surfaces.add(s)
    self.surface = s
    limit_append(self.history, "done")
    
def move(self, sep):
    input = convert_to_int(2, sep[1:])
    if not input:
        limit_append(self.history, "Usage: move <x> <y>")
        return
    location = (input[0], input[1])
    self.surface.location = location
    limit_append(self.history, "done")


def draw_box(surface):
    pygame.draw.line( surface.surface \
                    , color.Black \
                    , (0, 0) \
                    , (surface.size[0], 0))

    pygame.draw.line( surface.surface \
                    , color.Black \
                    , (0, 0) \
                    , (0, surface.size[1]))

    pygame.draw.line( surface.surface \
                    , color.Black \
                    , (surface.size[0] - 1, 0) \
                    , (surface.size[0] - 1, surface.size[1] - 1) ) 

    pygame.draw.line( surface.surface \
                    , color.Black \
                    , (0, surface.size[1] - 1) \
                    , (surface.size[0] - 1, surface.size[1] -1) )

def draw_entry_line(surface):
    pygame.draw.line( surface.surface \
                    , color.Black \
                    , (0, surface.size[1] - EntryLineOffset) \
                    , (surface.size[0], surface.size[1] - EntryLineOffset))

def draw_text(font, text, location, surface):
    text_surface = font.render(text, True, color.Black)
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



def limit_append(list, item):
    if len(list) > 100:
        list.pop()
    list.insert(0, item)

def convert_to_int(count, list):
    if len(list) != count:
        return None
    ret = []
    try:
        for l in list:
            ret.append(int(l)) 
    except ValueError:
        return None

    return ret

def init_console(engine_manager):
    s = SingleSurface(pygame.Surface((200, 200)), (10, 10), (200, 200), ConsolePriority)
    Surfaces.add(s)
    return Console(s, engine_manager)