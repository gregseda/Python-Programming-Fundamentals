"""Python Fundamentals Final Project - shapes module."""
# Greg Seda
import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.data = [x, y]

    def __getitem__(self, index):
        return self.data[index]

    def __iter__(self):
        yield self.x
        yield self.y

    def __repr__(self):
        return "Point(x={0}, y={1})".format(self.x, self.y)

    def __str__(self):
        return "Point at ({0}, {1})".format(self.x, self.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __imul__(self, scalar):
        self.x *= scalar
        self.y *= scalar
        return self

    def __mul__(self, scalar):
        return Point(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        return Point(scalar * self.x, scalar * self.y)

    def distance(self, other):
        return ((self.x - other.x)**2 + (self.y-other.y)**2)**0.5

    def loc_from_tuple(self, coords):
        self.x, self.y = coords

    @classmethod
    def from_tuple(cls, coords):
        x, y = coords
        return cls(x, y)

    @property
    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)


class Circle(Point):
    def __init__(self, center=None, radius=1):
        if center is None:
            center = Point(0, 0)
        self.center = center
        self.radius = radius

    def __getitem__(self, item):
        return self.center[item]

    def __str__(self):
        return "Circle with center at ({0}, {1}) and radius {2}".format(self.
                                                                        center.
                                                                        x,
                                                                        self.
                                                                        center.
                                                                        y,
                                                                        self.
                                                                        radius)

    def __repr__(self):
        return "Circle(center=Point({0}, {1}), radius={2})".format(self.
                                                                   center.x,
                                                                   self.
                                                                   center.y,
                                                                   self.
                                                                   radius)

    @property
    def center(self):
        return self._center

    @center.setter
    def center(self, center):
        if not isinstance(center, Point):
            raise TypeError("The center must be a Point!")
        self._center = center

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius < 0:
            raise ValueError('The radius cannot be negative!')
        self._radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

    @property
    def area(self):
        return math.pi * self.radius ** 2

    def __iadd__(self, other):
        self.center.x += other.center.x
        self.center.y += other.center.y
        self.radius += other.radius
        return self

    def __add__(self, other):
        return Circle(Point(self.center.x + other.center.x,
                            self.center.y+other.center.y),
                      self.radius+other.radius)

    @classmethod
    def from_tuple(cls, center, radius=1):
        return cls(Point(*center), radius)

    def center_from_tuple(self, center):
        self.center = Point.from_tuple(center)
