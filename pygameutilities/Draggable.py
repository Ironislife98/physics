import pygame.math
import pygame.mouse


def checkMouse():
    if pygame.mouse.get_pressed(num_buttons=3)[0]:
        print("pressed")