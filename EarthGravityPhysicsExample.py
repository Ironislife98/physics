import pygame
import SmallObject
import time
import Physics2D
import Collision2D

pygame.init()

WIDTH, HEIGHT = 1000, 900
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Physics Example")

obj1 = SmallObject.smallObject(100, 100, 100, 100, 100000, color=(255, 0, 0))
obj2 = SmallObject.smallObject(200, 800, 1000, 1000, 100000000, name="Ground1")
obj3 = SmallObject.smallObject(300, 100, 100, 100, 100000, color=(255, 0, 0))


gravObject = Physics2D.Gravity(windowHeight=HEIGHT)
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
    obj3.draw(win)

    collide = Collision2D.detectCollision(obj1, [obj2])
    if collide[0] and obj1.jumping:
        obj1.rect.bottom = collide[1].rect.top
        obj1.vector.y = obj1.rect.top
        obj1.jumping = False
    elif not collide[0] and obj1.jumping:
        movetowards = gravObject.update(obj1.rb.mass, obj2.rb.mass, pygame.math.Vector2(obj1.vector.x, obj1.vector.y), obj2.vector)
        obj1.vector.y = movetowards.y

    collide = Collision2D.detectCollision(obj3, [obj2])
    if collide[0] and obj3.jumping:
        obj3.rect.bottom = collide[1].rect.top
        obj3.vector.y = obj3.rect.top
        obj3.jumping = False
    elif not collide[0] and obj3.jumping:
        movetowards = gravObject.update(obj3.rb.mass, obj2.rb.mass, pygame.math.Vector2(obj3.vector.x, obj3.vector.y), obj2.vector)
        obj3.vector.y = movetowards.y
    
    if pygame.mouse.get_pressed()[0]:
        obj1.vector.xy = pygame.mouse.get_pos()
        obj1.jumping = True


    #print(obj1.vector, obj2.vector)
    pygame.display.update()