"""Homework 6 for CSE-41273"""
# Greg Seda
import itertools


# 1.  squash
def squash(matrix):
    """Return squashed list from list of lists"""
    squashed = list(itertools.chain.from_iterable(matrix))
    return squashed


# 2. special_nums
def special_nums():
    """Return list of numbers from 1 to 300 that are divisible by 10 and 6"""
    special_list = [n for n in range(1, 301) if n % 30 == 0]
    return special_list


# 3. switch_dict
def switch_dict(dictionary):
    """Return a new dictionary with keys and values switched"""
    new_dict = {x: y for y, x in dictionary.items()}
    return new_dict


# 4. is_prime
def is_prime(candidate):
    """Return True if candidate is a prime number. Made with one statement"""
    return not any(candidate % n == 0
                   for n in range(2, candidate))


# 5. number_9
def number_9():
    """Return a generator that always returns the number 9"""
    nine = itertools.repeat(9)
    return nine


# 6. reverse_iter
def reverse_iter(iterable):
    """Return a generator that yields items from iterable in reverse order"""
    index = len(iterable) - 1
    while index > -1:
        yield iterable[index]
        index -= 1


# 7. ReverseIter class
class ReverseIter:
    """Class whose instances iterate the initial iterable in reverse order"""
    def __init__(self, sequence):
        self.sequence = sequence
        self.index = len(sequence)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.sequence[self.index]
