
from database import Surfaces
from surface_management import SingleSurface
from resources import ResourceId
import color
import pygame

from comms.server import GameServer

ConsolePriority = 1


TextHeight = 15
HorizontalMargin = 10
EntryLineOffset = 18

class Console:

    def __init__(self, surface_id, engine_manager):
        self.active = False
        self.surface_id = surface_id
        self.engine_manager = engine_manager
        self.entry = []
        self.history = []
        self.commands = { "resize": lambda x, sep: resize(x, sep) \
                        , "move" : lambda x, sep: move(x, sep) \
                        , "quit" : lambda x, sep: close_program(x, sep) \
                        , "spawn" : lambda x, sep: spawn_id(x, sep) \
                        , "despawn" : lambda x, sep: despawn_id(x, sep) \
                        , "move_mob" : lambda x, sep: move_mob_id(x, sep) \
                        , "connect_to_server" : lambda x, sep: connect_to_server(x, sep) \
                        }

    def activate(self):
        self.active = True
        surface = Surfaces.get(self.surface_id)
        surface.visible = True

    def deactivate(self):
        self.active = False
        surface = Surfaces.get(self.surface_id)
        surface.visible = False

    def update(self):
        if self.active:
            surface = Surfaces.get(self.surface_id)
            surface.surface.fill(color.White)
            draw(surface, self.entry, self.history)
    
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
            self.deactivate()
        elif event.unicode:
            self.entry.append(event.unicode)

def connect_to_server(self, sep):
    values = sep[1].split(":")
    if len(values) != 2:
        limit_append(self.history, "Usage: connect_to_server x.y.z.w:port")
        return
    port_list = convert_to_int(1, values[1:])
    if not port_list:
        limit_append(self.history, "port must be an integer")
        return

    port = port_list[0]

    limit_append(self.history, f"Attempting to connect to {values[0]}:{port}")
    success = GameServer.connect_to_server(values[0], port)
    if not success:
        limit_append(self.history, "Connection Failed")

def move_mob_id(self, sep):
    input = convert_to_int(3, sep[1:])
    if not input:
        limit_append(self.history, "Usage move_mob: <id> <x> <y>")
        return
    result = self.engine_manager.move(input[0], (input[1], input[2]))
    if result:
        limit_append(self.history, "done")
    else:
        limit_append(self.history, "move failed")

def despawn_id(self, sep):
    input = convert_to_int(1, sep[1:])
    if not input:
        limit_append(self.history, "Usage despawn: <id>")
        return
    self.engine_manager.despawn(input[0])
    limit_append(self.history, "done")

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
    old_surface = Surfaces.get(self.surface_id)
    Surfaces.remove(self.surface_id)
    s = SingleSurface(pygame.Surface(size), old_surface.location, size, ConsolePriority)
    id = Surfaces.add(s)
    self.surface_id = id
    limit_append(self.history, "done")
    
def move(self, sep):
    input = convert_to_int(2, sep[1:])
    if not input:
        limit_append(self.history, "Usage: move <x> <y>")
        return
    location = (input[0], input[1])
    surface = Surfaces.get(self.surface_id)
    surface.location = location
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
    s.visible = False
    id = Surfaces.add(s)
    return Console(id, engine_manager)