from pygame.math import Vector2
import pygame
from Attractor import Attractor


class smallObject(Attractor):
    def __init__(self, x, y, width, height, color=(0, 0, 0)):
        super().__init__()
        self.vector = Vector2(x, y)
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.vector.x, self.vector.y, self.width, self.height)
        self.color = color

    def draw(self, surface):
        self.rect = pygame.Rect(self.vector.x, self.vector.y, self.width, self.height)
        pygame.draw.rect(surface, self.color, self.rect)