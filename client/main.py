
# Location is X, Y
# Size is W, H

import pygame

from database import init_local_database 
from surface_management import AggregateSurface, SingleSurface, init_main_screen
from console import init_console

EventLoopWait = 16
DefaultHeight = 500
DefaultWidth = 800
White = [255, 255, 255]

local_database = init_local_database()

pygame.init()

main_screen = init_main_screen(local_database, DefaultWidth, DefaultHeight)
console = init_console(local_database, main_screen)


loop_start = 0

active = True
event_loop_delta = 0

while active:
    ticks = pygame.time.get_ticks()
    event_loop_delta = ticks - loop_start
    loop_start = ticks

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:

            if console.active:
                console.process_key(event)

            if event.mod & pygame.KMOD_SHIFT and event.key == pygame.K_SEMICOLON:
                console.active = True

        elif event.type == pygame.KEYUP:
            pass
        elif event.type == pygame.MOUSEBUTTONDOWN: 
            pass
        elif event.type == pygame.MOUSEBUTTONUP: 
            pass
        elif event.type == pygame.VIDEORESIZE:
            main_screen.size = (event.w, event.h)
        elif event.type == pygame.QUIT:
            active = False

    # redraw the main screen
    console.update_surface()

    main_screen.surface.fill(White)
    main_screen.update()
    pygame.display.update()

    loop_end = pygame.time.get_ticks()

    loop_duration = loop_end - loop_start

    if loop_duration < EventLoopWait:
        pygame.time.delay(EventLoopWait - loop_duration)
    