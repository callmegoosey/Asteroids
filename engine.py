import pygame
from constants import * 

class Engine:
    __screen = pygame

    def __init__():
        
        Engine.__window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        
        print("Starting asteroids!")
        print(f"Screen width: {SCREEN_WIDTH}")
        print(f"Screen height: {SCREEN_HEIGHT}")

    def game_loop():
        while(True):
            #Engine.__pygame.display.fi.surface.fill((255,255,255))
            pygame.Surface.fill(Engine.__window, (255,255,0))

            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    return

            pygame.display.flip()
