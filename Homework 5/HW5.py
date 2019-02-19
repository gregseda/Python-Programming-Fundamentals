"""Homework 5 for CSE-41273"""
# Greg Seda
import math
from functools import total_ordering


# Part 1
class Circle:
    """Class to create Circle objects"""

    def __init__(self, radius=1):
        """Circle initializer"""
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative!")
        self._radius = getattr(self, '_radius', None)
        self._radius_log = getattr(self, '_radius_log', [])
        self._radius = value
        self._radius_log.append(value)

    @property
    def radius_log(self):
        return self._radius_log[:]

    @property
    def area(self):
        """Calculate and return the area of the Circle"""
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        """Calculate and return the diameter of the Circle"""
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        """Set the diameter"""
        self.radius = diameter / 2

    def __str__(self):
        return "Circle of radius {}".format(self.radius)

    def __repr__(self):
        return "Circle(radius={})".format(self.radius)




# Part 2
@total_ordering
class BankAccount:
    """ Simple BankAccount class """

    def __init__(self, balance=0):
        """Initialize account with balance"""
        self.balance = balance

    def deposit(self, amount):
        """Deposit amount to this account"""
        self.balance += amount

    def withdraw(self, amount):
        """Withdraw amount from this account"""
        self.balance -= amount

    def __str__(self):
        return "Account with balance of ${}".format(self.balance)

    def __repr__(self):
        return "BankAccount(balance={})".format(self.balance)

    def __bool__(self):
        if self.balance <= 0:
            return False
        else:
            return True

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance
