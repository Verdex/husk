
# Location is X, Y
# Size is W, H

import pygame

from database import LocalIdManager
from surface_management import AggregateSurface, SingleSurface

EventLoopWait = 16
DefaultHeight = 500
DefaultWidth = 800
White = [255, 255, 255]

local_id_manager = LocalIdManager()

pygame.init()

best_depth = pygame.display.mode_ok((DefaultWidth, DefaultHeight), 0, 32)
screen = pygame.display.set_mode((DefaultWidth, DefaultHeight), pygame.RESIZABLE, best_depth) 


loop_start = 0

# TODO 
active = True
event_loop_delta = 0

while active:
    ticks = pygame.time.get_ticks()
    event_loop_delta = ticks - loop_start
    loop_start = ticks

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            pass
        elif event.type == pygame.KEYUP:
            pass
        elif event.type == pygame.MOUSEBUTTONDOWN: 
            pass
        elif event.type == pygame.MOUSEBUTTONUP: 
            pass
        elif event.type == pygame.VIDEORESIZE:
            pass
        elif event.type == pygame.QUIT:
            pass


    # TODO Update

    loop_end = pygame.time.get_ticks()

    loop_duration = loop_end - loop_start

    if loop_duration < EventLoopWait:
        pygame.time.delay(EventLoopWait - loop_duration)
    