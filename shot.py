from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, pos = pygame.Vector2, radius = int):
        self.position = pos
        self.radius = radius
        pygame.sprite.Sprite.__init__(self, (DRAWABLE, UPDATABLE, PROJECTILES))

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,0), self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt