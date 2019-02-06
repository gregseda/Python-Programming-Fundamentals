""" CLI program to test HW3 homework """
# Greg Seda
# For each test function, test *all* the cases shown in the instructions
import argparse
from HW3 import words_containing, len_safe, unique


def test_words_containing():
    """Return True/False if the test of words_containing passes/fails"""
    sentence = "Anyone who has never made a mistake has never tried anything"
    sentence2 = "The cow jumped over the moon"
    new_list = words_containing(sentence, 'a')
    new_list2 = words_containing(sentence, 'x')
    new_list3 = words_containing('', 'x')
    new_list4 = words_containing(sentence2, 't')

    if new_list == [
                    'Anyone', 'has', 'made',
                    'a', 'mistake', 'has', 'anything']:
        if new_list2 == []:
            if new_list3 == []:
                if new_list4 == ['The', 'the']:
                    return True
    else:
        return False


def test_len_safe():
    """Return True/False if the test of len_safe passes/fails"""
    my_dict = {'a': 23, 'b': 8}
    x = len_safe(my_dict)
    y = len_safe([])
    z = len_safe(0.25)
    n = len_safe(7)
    m = len_safe('cat')
    p = len_safe('')
    animals = ['dog', 'cat', 'bird', 'cat', 'fish']
    q = len_safe(animals)

    if x == 2:
        if y == 0:
            if z == -1:
                if n == -1:
                    if m == 3:
                        if p == 0:
                            if q == 5:
                                return True
    else:
        return False


def test_unique():
    """Return True/False if the test of unique passes/fails"""
    numbers = [4, 5, 2, 6, 2, 3, 5, 8]
    nums = unique(numbers)
    try:
        x = next(nums)
        y = next(nums)
        z = next(nums)
        m = next(nums)
        n = next(nums)
        q = next(nums)
        if x == 4:
            if y == 5:
                if z == 2:
                    if m == 6:
                        if n == 3:
                            if q == 8:
                                next(nums)
    except StopIteration:
        return True
    return False


if __name__ == "__main__":
    # Set up argparse information here
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--unique",
                        help="Flag to test the unique function from HW3",
                        action="store_true")
    parser.add_argument("-w", "--words",
                        help="Flag to test words_containing function from HW3",
                        action="store_true")
    parser.add_argument("-l", "--len",
                        help="Flag to test the len_safe function from HW3",
                        action="store_true")
    args = parser.parse_args()

    # Based on user input, run test(s) requested and print results
    # The ONLY printing should happen here. No other parts of the code
    # should print things.
    if args.unique:
        if test_unique():
            print("unique passed")
        else:
            print("unique failed")
    if args.words:
        if test_words_containing():
            print("words passed")
        else:
            print("words failed")
    if args.len:
        if test_len_safe():
            print("len_safe passed")
        else:
            print("len_safe failed")
