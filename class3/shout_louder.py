"""
Shout louder
=====
Do you remember the shout function that you wrote that appended exclamation points to a string?  Write a function called shout_louder that takes two arguments - a string called words and a number called n.  shout_louder(words, n) will append "n" number of exclamation points to the word.  What happens if you pass in a non-numeric type as the second argument, n?  Make sure an error doesn't occur!

Example Output (after importing into Python interactive shell):

>>> from shout_louder import *
>>> shout_louder("You should be whispering", 5)
'You should be whispering!!!!!'
"""

def shout_louder(words,n):
    try:
        var=int(n)
        print words+('!'*n)
    except (TypeError, ValueError, NameError):
        print 'Not an integer'