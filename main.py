import pygame
import pygame.math
import sys
import math
import time
import PhysicsEngine
from pygame.sprite import Sprite

pygame.init()
startTime = time.time()
WIDTH, HEIGHT = 1000, 900

floorObjects = []


class Player(Sprite):
    def __init__(self, x, y, width, height, vel=12):
        self.mass = 1

        self.vector = pygame.Vector2()
        self.vector.x = x
        self.vector.y = y
        self.velocity = pygame.Vector2(0, 0)

        self.color = (255, 0, 0)
        self.width = width
        self.height = height
        self.vel = 12
        self.engine = PhysicsEngine.PhysicsEngine()

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((255, 0, 0))
        self.rect = pygame.Rect(self.vector.x, self.vector.y, self.width, self.height)

        self.jumping = True

    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            self.velocity.y = -self.vel
        if pressed[pygame.K_s]:
            self.velocity.y = self.vel
        if pressed[pygame.K_a]:
            self.velocity.x = -self.vel
        if pressed[pygame.K_d]:
            self.velocity.x = self.vel
        self.vector.xy += self.velocity.xy
        self.velocity.xy = 0, 0

    def Physics(self, floorobjects, groundObjects):
        self.engine.verticalCollision(self, [ground])

    def draw(self):
        self.rect = pygame.Rect(self.vector.x, self.vector.y, self.width, self.height)
        pygame.draw.rect(window, self.color, self.rect)


class Ground(Sprite):
    def __init__(self, x=0, y=800):
        self.vector = pygame.Vector2()
        self.vector.x = x
        self.vector.y = y
        self.width, self.height = 1000, 1000
        self.color = (0, 0, 0)
        self.rect = pygame.Rect(self.vector.x, self.vector.y, self.width, self.height)

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((255, 0, 0))
        floorObjects.append(self)
    
    def draw(self):
        pygame.draw.rect(window, self.color, self.rect)


def drawAll():
    window.fill((255, 255, 255))

    ground.draw()
    p.Physics(floorObjects, ground)
    p.draw()

   

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