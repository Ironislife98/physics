import pygame.math
import pygame


def move_object(objectRect: pygame.Rect, mousepoint: pygame.Vector2) -> pygame.Vector2 or None:
    """Takes in a pygame rect object and checks if mouse collides with it, if it does
        the it returns the xy values of the object to move to, if it does not, it returns None"""
    if objectRect.collidepoint(mousepoint.x, mousepoint.y):
        return mousepoint
    else:
        return None
