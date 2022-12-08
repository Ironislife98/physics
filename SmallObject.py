from pygame.math import Vector2
import pygame
from Physics2D import RigidBody2D, Attractor


# All objects need a .name
class smallObject(Attractor):
    def __init__(self, x, y, width, height, mass, name="smallObject", autoDefineBottom=True, bottom=pygame.math.Vector2(), color=(0, 0, 0)):
        self.vector = Vector2(x, y)
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.vector.x, self.vector.y, self.width, self.height)
        self.color = color
        self.rb = RigidBody2D(mass, drag=1)
        self.name = name
        self.jumping = True

        if autoDefineBottom:
            print(self.rect.bottom)
            self.bottom = pygame.math.Vector2(self.rect.centerx, self.rect.bottom)
        else:
            self.bottom = bottom

        super().__init__(self.rb, childClass=self)

    def draw(self, surface):
        self.rect = pygame.Rect(self.vector.x, self.vector.y, self.width, self.height)
        self.bottom = pygame.math.Vector2(self.rect.centerx, self.rect.bottom)
        pygame.draw.rect(surface, self.color, self.rect)