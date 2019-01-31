
"""
try:
    int('one')
except ValueError:
    print("Can't convert that to integer")"""

"""
try:
    print("This code might raise an exception")
except Exception1:
    print("If Exception1 happens, we come to this block.")
    raise
except Exception2:
    print("If Exception2 happens, we come to this block.")
else
    print("Optionally, this block is when there are no exceptions.")
print("After all is done we continue here,")
print("Unless an unhandled exception occured")
print("or we re-raised the exception.")
"""

"""
try:
    print("This code might raise an exception")
except (Exception1, Exception2)
    print("If Exception1 or Exception2 happens, we come here")
finally:
    print("This block is always executed before leaving try-except")
print("after all is done we continue here,")
print("Unless an unhandled exception occured")
print("or we re-raised the exception")
"""


things = [2.5, 'one']
for thing in things:
    try:
        print("In try block, going to convert {}"
            .format(repr(thing)))
        new_int = int(thing)
        print("After conerting to int: {}".format(new_int))
    except ValueError:
        print("ValueError: Can't conert {} to integer"
            .format(repr(thing)))
    else:
        print("Yay! No error occured this time!")
    finally:
        print("Finally!")
    print("after the try is finished\n")
print("The loop is finished")
