""" Homework assignment for week 3 """
# Greg Seda


def words_containing(sentence, letter):
    """ Given a sentence, returns list of words that contain the letter.
        Letter given is lowercase. Sentence can be mixed case, and the
        case should be ignored for searching.
    """
    word_list = sentence.split()
    upper = letter.upper()
    word_list1 = [word for word in word_list if word.count(letter) >= 1]
    word_list2 = [word for word in word_list if word.count(upper) >= 1]
    return word_list2 + word_list1


def len_safe(object):
    """Return length of object or -1 if object has no length."""
    try:
        return len(object)
    except ValueError:
        return -1
    except TypeError:
        return -1


def unique(iterable):
    """Yield iterable elements in order, skipping duplicate values."""
    num_check = set()
    for nums in iterable:
        if nums not in num_check:
            num_check.add(nums)
            yield nums
