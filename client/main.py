
# Location is X, Y
# Size is W, H

import pygame

pygame.init()

from database import init_local_database 
from surface_management import AggregateSurface \
                             , SingleSurface \
                             , init_main_screen 
from engine.game_field import Field
from console import init_console
from engine.management import EngineManager
import color

EventLoopWait = 16
DefaultHeight = 500
DefaultWidth = 800

local_database = init_local_database()

main_screen = init_main_screen(local_database, DefaultWidth, DefaultHeight)
game_field = Field(local_database, main_screen, (DefaultWidth, DefaultHeight))
engine_manager = EngineManager(local_database, game_field)
console = init_console(local_database, main_screen, engine_manager)


loop_start = 0

event_loop_delta = 0

while engine_manager.active:
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
            game_field.resize(main_screen.size)
        elif event.type == pygame.QUIT:
            engine_manager.active = False

    # redraw the main screen
    console.update_surface()
    game_field.update()
    main_screen.surface.fill(color.White)
    main_screen.update()
    pygame.display.update()

    loop_end = pygame.time.get_ticks()

    loop_duration = loop_end - loop_start

    if loop_duration < EventLoopWait:
        pygame.time.delay(EventLoopWait - loop_duration)
    