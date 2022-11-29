import pygame
import pygame.math
import sys

pygame.init()

WIDTH, HEIGHT = 1000, 900
window = pygame.display.set_mode((WIDTH, HEIGHT))
GRAVITYFORCE = 10


class Player:
    def __init__(self, x, y) -> None:
        self.vector = pygame.Vector2()
        self.vector.xy = x, y
        self.width = 100
        self.height = 100
        self.image = pygame.draw.circle(window, (0, 0, 0), self.vector.xy, 20)
    
    def gravity(self, large):
        g = (GRAVITYFORCE * large.mass) / (large.radius ** 2)

    def draw(self):
        return pygame.draw.circle(window, (0, 0, 0), self.vector.xy, 20)


class LargeMass:
    def __init__(self, mass, x, y, radius) -> None:
        self.mass = mass
        self.vector = pygame.Vector2()
        self.vector.xy = x, y
        self.radius = radius
    
    def draw(self):
        return pygame.draw.circle(window, (0, 0, 0), self.vector.xy, self.radius)

def draw():
    window.fill((255, 255, 255))
    p.draw()
    largemass.draw()


def destroy():
    global run
    pygame.quit()
    run = False
    sys.exit()

p = Player(400, 100)
largemass = LargeMass(1000, 400, 400, 100)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            destroy()

    draw()
    p.gravity(largemass)
    pygame.display.update()


sys.exit()