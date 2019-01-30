"""Homework 2 for CSE-41273"""
# Greg Seda


# Function 1
def combine_lists(one, two):
    """Take 2 lists as input and return a new list consisting of the elements
        of the first list followed by the elements of the second list"""
    combined_list = one + two
    return combined_list


# Function 2
def last_n_elements(sequence, n):
    """Given a sequence and a number n, return the last n elements of the
        sequence"""
    new_sequence = sequence[-n:]
    return new_sequence


# Function 3
def last_n_reversed(sequence, n):
    """Given a sequence and a number n, return the last n elements of the
        sequence in reversed order"""
    sequence = sequence[::-1]
    new_sequence = sequence[:n]

    return new_sequence


# Function 4
def power_list(numbers):
    """Given a list of numbers, return a new list where each element is the
        corresponding element of the list to the power of the list index"""
    powered_numbers = [
        n ** x
        for x,
        n in enumerate(numbers)
    ]

    return powered_numbers


# Function 5
def rotate_list(some_list):
    """Take a list as input and remove the first item from the list and add it
        to the end of the list. Return the item moved"""
    list_length = len(some_list)
    list_length -= 1
    item_removed = some_list.pop(0)
    some_list.insert(list_length, item_removed)

    return item_removed


# Function 6
def matrix_fill(n_rows, n_cols):
    """Given number of rows and number of columns, create a matrix (list of
        lists) where each element is sequentially numbered"""
    filled_matrix = [
        [x for x
            in range(1, n_rows * n_cols + 1)]
        [i:i + n_cols]
        for i in range(0, n_rows * n_cols, n_cols)
    ]

    return filled_matrix


# Function 7
def get_word_codes(words):
    """Given a list of words, return a dictionary where the words are keys,
        and the value for each key is a list of the character codes of the
        letters of the word that is its key"""
    codes = {
        key: [ord(code)
              for code in key]
        for key in words
    }

    return codes
