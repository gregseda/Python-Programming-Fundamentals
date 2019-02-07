"""Homework 4 for CSE-41273"""
# Greg Seda
import math


class Person:
    """Person with first and last name."""
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

    @property
    def name(self):
        return self.last_name + ", " + self.first_name


class Point:
    """2-D Point objects."""
    def __init__(self, x=0, y=0):
        """Initialize the Point instance"""
        self.x = x
        self.y = y

    @property
    def magnitude(self):
        """Return the magnitude of vector from (0,0) to self."""
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __str__(self):
        return "Point at ({}, {})".format(self.x, self.y)

    def __repr__(self):
        return "Point(x={}, y={})".format(self.x, self.y)
