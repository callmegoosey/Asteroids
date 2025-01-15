from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, (DRAWABLE, UPDATABLE, PROJECTILES))
