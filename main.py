import pygame
import pygame.math
import sys
import math
import time
import PhysicsEngine
from pygame.sprite import Sprite

pygame.init()
starttime = time.time()
WIDTH, HEIGHT = 1000, 900

class Player(Sprite):
    def __init__(self, x, y, width, height, vel=12):
        self.mass = 1
        self.vector = pygame.Vector2()
        self.vector.x = x
        self.vector.y = y
        self.color = (255, 0, 0)
        self.width = width
        self.height = height
        self.vel = 12
        self.engine = PhysicsEngine.PhysicsEngine()
    
    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            self.vector.y -= self.vel
        if pressed[pygame.K_s]:
            self.vector.y += self.vel
        if pressed[pygame.K_a]:
            self.vector.x -= self.vel
        if pressed[pygame.K_d]:
            self.vector.x += self.vel

    def Physics(self, largemass):
        self.vector.y += self.engine.earthGravity(self.mass, largemass.vector.y, self.vector.y)

    def draw(self):
        self.Rect = pygame.Rect(self.vector.x, self.vector.y, self.width, self.height)
        pygame.draw.rect(window, self.color, self.Rect)


class Ground(Sprite):
    def __init__(self, x=0, y=800):
        self.vector = pygame.Vector2()
        self.vector.x = x
        self.vector.y = y
        self.width, self.height = 1000, 1000
        self.color = (0, 0, 0)
    
    def draw(self):
        self.Rect = pygame.Rect(self.vector.x, self.vector.y, self.width, self.height)
        pygame.draw.rect(window, self.color, self.Rect)

def drawAll():
    window.fill((255, 255, 255))
    ground.draw()
    p.draw()
    p.Physics(ground)
   

window = pygame.display.set_mode((WIDTH, HEIGHT))
Clock = pygame.time.Clock()
FRAMERATE = 60

p = Player(400, 100, 100, 100)
ground = Ground()
run = True
while run:
    Clock.tick(FRAMERATE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    
    p.move()

    drawAll()

    pygame.display.update()

pygame.quit()
sys.exit()