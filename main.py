import pygame
import SmallObject



pygame.init()

WIDTH, HEIGHT = 1000, 900
win = pygame.display.set_mode((WIDTH, HEIGHT))


obj1 = SmallObject.smallObject(100, 100, 100, 100, 100)
obj2 = SmallObject.smallObject(400, 500, 100, 100, 100)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
    win.fill((255, 255, 255))

    obj1.draw(win)
    obj2.draw(win)


    obj1.Update()
    obj2.Update()
    
    pygame.display.update()