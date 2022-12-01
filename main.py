import pygame
import pygame.math
import sys
import math

pygame.init()

WIDTH, HEIGHT = 1000, 900

class Player:
    def __init__(self, x, y, width, height, vel=12):
        self.mass = 6
        self.vector = pygame.Vector2()
        self.vector.x = x
        self.vector.y = y
        self.color = (255, 0, 0)
        self.width = width
        self.height = height
        self.vel = 12
    
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
        # distance = (6.4 * (10 ** 6)) ** 2
        #? Refactor to just largemass.vector.y - self.vector.y
        #? Because y value of self should always be above ground
        #? Could change to add empty vector to just track where the ground is
        distance = max(largemass.vector.y, self.vector.y) - min(largemass.vector.y, self.vector.y)
        force = ((6.67 * (10 ** -11)) * (6 * 10 ** 24) * self.mass) / distance
        print(force)
        self.vector.y += force


    def draw(self):
        self.Rect = pygame.Rect(self.vector.x, self.vector.y, self.width, self.height)
        pygame.draw.rect(window, self.color, self.Rect)


class Ground:
    def __init__(self):
        self.x = 0
        self.y = 800
        self.width, self.height = 1000, 1000
        self.color = (0, 0, 0)
    
    def draw(self):
        self.Rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(window, self.color, self.Rect)

def drawAll():
    window.fill((255, 255, 255))
    p.draw()
    p.Physics(ground)
    ground.draw()

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