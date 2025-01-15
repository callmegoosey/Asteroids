from circleshape import CircleShape
from constants import *
import pygame

class Player(CircleShape):
    
    _rotation = 0
    
    def __init__(self, x = int, y = int):
        super().__init__(x, y, PLAYER_RADIUS)
        _rotation = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self._rotation)
        right = pygame.Vector2(0, 1).rotate(self._rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (0,0,0), self.triangle(), 2)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

    def rotate(self, dt):
        self._rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self._rotation)
        self.position += forward * PLAYER_SPEED * dt