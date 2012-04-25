"""
add_three_tested.py
=====
Create a function that takes one argument, n.  Return n with 3 added to it.  Write doc tests.

http://docs.python.org/library/doctest.html
"""

def add_3(n):
    return (n+3)

from add_three_tested import *
print add_3(3)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
