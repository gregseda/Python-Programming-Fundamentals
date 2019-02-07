import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    def get_magnitude(point):
        return math.sqrt(point.x ** 2 + point.y ** 2)

class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2
