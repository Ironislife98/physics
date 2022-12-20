import pygame
import math
import time
from functools import wraps
from typing import Callable

pygame.init()

WIDTH, HEIGHT = 1000, 900
win = pygame.display.set_mode((WIDTH, HEIGHT))


clock = pygame.time.Clock()

startx, starty = -100, 300
x, y = startx, starty
rect = pygame.draw.rect(win, (255, 0, 0), pygame.Rect(x, y, 10, 10))


def memoize(func: Callable):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

# Memoize doesnt really help in this situation
# Unless your computer is a potato
# But its a slight speed improvement
@memoize
def movesine(dt: float, scale: float):
    global starty, startx
    return dt * scale, starty + math.sin(dt) * scale


def handleoffscreen():
    global x, WIDTH, win, starttime
    if x >= WIDTH:
        starttime = time.time()
        win.fill((255, 255, 255))
        x = startx



win.fill((255, 255, 255))
starttime = time.time()
while True:
    clock.tick(1000000000000000000000000000000000)
    dt = time.time() - starttime
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
    x, y = movesine(dt=dt, scale=100)
    handleoffscreen()
    #pygame.draw.rect(win, (255, 0, 0), pygame.Rect(x, y, 5, 5))
    pygame.draw.circle(win, (255, 0, 0), (x, y), 1)
    pygame.display.update()