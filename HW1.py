"""Homework 1 for CSE-41273"""
# Greg Seda


# Function 1
def silly_case(in_string):
    """Given a string, convert it to a string such that each word starts with
        a lower case letter, and the remaining letters are uppercase.
        Return the silly case string."""
    s = in_string.title()
    s = s.swapcase()
    return s


# Function 2
def dash_stringify(word_list):
    """Given a list of word strings, return a single string with all the
        strings together, with ' - ' in between the words."""
    s = " - ".join(word_list)
    return s


# Function 3
def is_perfect_square(number):
    """Given a number, return True if it is a perfect square,
        else return False"""
    x = float(number)
    x = x ** 0.5
    y = int(x)
    return (x == y)


# Function 4
def is_leap_year(year):
    """Given a year, return True if it is a leap year, else return False"""
    x = year % 4
    y = year % 100
    z = year % 400

    if y == 0:
        return (z is 0)
    else:
        return (x is 0)
