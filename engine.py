import pygame
from constants import * 
from player import * 

class Engine:
    __screen = pygame
    __clock = pygame.time.Clock()
    __dt = None
    __player = Player
    __updatable = pygame.sprite.Group
    __drawable = pygame.sprite.Group

    def __init__():
        
        Engine.__window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        Engine.__dt = 0

        Engine.__player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

        Engine.__updatable = pygame.sprite.Group()
        Engine.__updatable.add(Engine.__player)

        Engine.__drawable = pygame.sprite.Group()
        Engine.__drawable.add(Engine.__player)

        print("Starting asteroids!")
        print(f"Screen width: {SCREEN_WIDTH}")
        print(f"Screen height: {SCREEN_HEIGHT}")

    def game_loop():

        Player.containers = (Engine.__updatable, Engine.__drawable)

        while(True):

            for object in Engine.__updatable:
                object.update(Engine.__dt)

            pygame.Surface.fill(Engine.__window, (255,255,0))
            

            for object in Engine.__drawable:
                object.draw(Engine.__window)



            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    return

            Engine.__dt = Engine.__clock.tick(60) / 1000
            #print(Engine.__dt)
            pygame.display.flip()
            
