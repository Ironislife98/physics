import pygame
import SmallObject
import time

pygame.init()

WIDTH, HEIGHT = 1000, 900
win = pygame.display.set_mode((WIDTH, HEIGHT))

RECT = pygame.Rect(100, 200, 100, 100)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            break
    win.fill((255, 255, 255))

    pygame.draw.rect(win, (255, 0, 0), pygame.Rect(RECT.centerx - 5, RECT.bottom, 10, 10))
    pygame.draw.rect(win, (0, 0, 0), RECT)
    pygame.display.update()