"""
Larger Than Five
=====
Convert larger_than_five.py into a function called larger_than_five that takes a list and returns a list of numbers larger than five.

Example Output (if imported into interactive shell):
>>> from larger_than_five_func import *
>>> larger_than_five(range(10))
[6, 7, 8, 9]
"""
def larger_than_five(list):
    big_numbers=[]
    for x in list:
        if x>5:
            big_numbers.append(x)
    return big_numbers