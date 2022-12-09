import pygame
import SmallObject
import time
import Physics2D
import Collision2D

pygame.init()

WIDTH, HEIGHT = 1000, 900
win = pygame.display.set_mode((WIDTH, HEIGHT))


obj1 = SmallObject.smallObject(100, 100, 100, 100, 100000, color=(255, 0, 0))
obj2 = SmallObject.smallObject(200, 800, 1000, 1000, 100000000, name="Ground1")

gravObject = Physics2D.Gravity()
gravObject.precomputeGround([obj2.rect])

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            break


    win.fill((255, 255, 255))
    obj2.draw(win)
    obj1.draw(win)

    #gravObject.findGround(win, HEIGHT, obj1.vector.x, [obj2.rect])

    collide = Collision2D.detectCollision(obj1, [obj2])
    if collide[0] and obj1.jumping:
        obj1.rect.bottom = collide[1].rect.top
        obj1.vector.y = obj1.rect.top
        obj1.jumping = False
        print("colllide")
        #obj1.vector = pygame.math.Vector2(10, 100)
    elif not collide[0] and obj1.jumping:
        movetowards = gravObject.update(obj1.rb.mass, obj2.rb.mass, pygame.math.Vector2(obj1.vector.x, obj1.vector.y), obj2.vector)
        obj1.vector.y = movetowards.y
        #print("move down")
    #print(movetowards)
    
    if pygame.mouse.get_pressed()[0]:
        obj1.vector.xy = pygame.mouse.get_pos()
        obj1.jumping = True


    #print(obj1.vector, obj2.vector)
    pygame.display.update()