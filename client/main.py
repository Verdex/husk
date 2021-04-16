
# Location is X, Y
# Size is W, H

import pygame

from database import init_local_database 
from surface_management import AggregateSurface, SingleSurface, init_main_screen

EventLoopWait = 16
DefaultHeight = 500
DefaultWidth = 800
White = [255, 255, 255]

local_database = init_local_database()

pygame.init()

main_screen = init_main_screen(local_database, DefaultWidth, DefaultHeight)

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
            active = False

    # redraw the main screen
    main_screen.surface.fill(White)
    main_screen.update()
    pygame.display.update()

    loop_end = pygame.time.get_ticks()

    loop_duration = loop_end - loop_start

    if loop_duration < EventLoopWait:
        pygame.time.delay(EventLoopWait - loop_duration)
    