import pygame
from constants import * 
from player import * 
from asteroid import *
from asteroidfield import *

class Engine():

    def __init__(self):
        self._clock = pygame.time.Clock()
        self._dt = None

        self._window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self._dt = 0

        self._player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

        # self._updatable = pygame.sprite.Group()
        # self._updatable.add(self._player)

        # self._drawable = pygame.sprite.Group()
        # self._drawable.add(self._player)

        #self._asteroids = pygame.sprite.Group()
        #Asteroid.containers = (self._asteroids, self._updatable, self._drawable)

        self._asteroid_field = AsteroidField()
        
        print("Starting asteroids!")
        print(f"Screen width: {SCREEN_WIDTH}")
        print(f"Screen height: {SCREEN_HEIGHT}")

    def game_loop(self):
        while(True):
            pygame.Surface.fill(self._window, (0,0,0))
            
            for object in UPDATABLE:
                object.update(self._dt)

            for object in ASTEROIDS:
                if object.collide_with(self._player):
                    raise Exception("Game over!")

            for object in DRAWABLE:
                object.draw(self._window)

            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    return

            self._dt = self._clock.tick(60) / 1000
            #print(Engine.__dt)
            pygame.display.flip()
            
