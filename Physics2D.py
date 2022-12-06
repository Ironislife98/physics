import pygame.math
import math

Attractors = []


class RigidBody2D:
    def __init__(self, mass, drag):
        self.mass = mass
        self.drag = drag

    def addForce(self, initialVector, moveTowards, force):
        """Takes in initialVector and forceVector and returns Vector2 of initalVector moved towards a vector by a force"""
        return initialVector.move_towards(moveTowards.xy, 100)


class Attractor:
    def __init__(self, RigidBody, childClass):
        self.childClass = childClass
        Attractors.append(self.childClass)

    def Update(self):
        for attractor in Attractors:
            self.Attract(attractor)

    def Attract(self, objToAttract):
        """
        All params need to have .vector -> pygame.Vector2 and .mass -> int/float values
        """
        # F = ((m1 * m2) / d^2) * G
        direction = self.childClass.vector - objToAttract.vector
        distance = direction.magnitude()
        try:
            forcemagnitude = (self.childClass.rb.mass * objToAttract.rb.mass) / math.pow(distance, 2)
            # Calculate Euclidian distance Instead
            force = direction.normalize() * forcemagnitude
        except ZeroDivisionError:
            force = pygame.math.Vector2(0, 0)
        print(force.xy)
        # Add some force
        # How?
        # return pygame.math.Vector2.move_towards(objToAttract.vector, force)
        return self.rb.addForce(self.childClass.vector, objToAttract.vector, force)
