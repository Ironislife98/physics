import pygame.math


class Attractor:
    def __init__(self):
        pass

    def Attract(self, selfobj, objToAttract):
        """
        All params need to have .vector -> pygame.Vector2 and .mass values
        :param selfobj:
        :param objToAttract:
        :return:
        """
        # F = ((m1 * m2) / d^2) * G
        direction = selfobj - objToAttract
        distance = direction.magnitude

        forcemagnitude = (selfobj.mass * objToAttract.mass) / pow(distance, 2)
        force = direction.normalized * forcemagnitude

        # Add some force
        # How?
        return pygame.math.Vector2.move_towards(objToAttract.vector, force)
