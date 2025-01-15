from circleshape import CircleShape
from constants import *

import random
import pygame

class Asteroid(CircleShape):
    def __init__(self, x = int, y = int, radius = int):
        self.position = pygame.Vector2(x, y)
        self.radius = radius
        pygame.sprite.Sprite.__init__(self, (DRAWABLE, UPDATABLE, ASTEROIDS))

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        pygame.sprite.Sprite.kill(self)

        if(self.radius <= ASTEROID_MIN_RADIUS):
            return
        
        for i in range(-1,2,2):
            a = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            a.velocity = self.velocity.copy().rotate(random.uniform(20,50) * i) * 1.2



    
