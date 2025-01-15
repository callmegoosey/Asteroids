from circleshape import CircleShape
import pygame
from constants import UPDATABLE, DRAWABLE, ASTEROIDS

class Asteroid(CircleShape):
    def __init__(self, x = int, y = int, radius = int):
        _pos = pygame.Vector2(x, y)
        _radius = radius
        pygame.sprite.Sprite.__init__(self, (DRAWABLE, UPDATABLE, ASTEROIDS))

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self._pos, self.__radius)

    def update(self, dt):
        self.pos += super().velocity * dt
