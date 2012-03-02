"""
Shout
=====
Write a function called shout.  Shout takes one parameter - a string that we'll call "words".  The resulting function definition should be be shout(words).  It will append three exclamation points to the input string, and return the new string.

Example Output (after importing into Python interactive shell):

>>> from shout import *
>>> # note that shout returns a string (notice the quotes)
... shout("I'm yelling")
"I'm yelling!!!"

>>> # you can print that string...
... print shout("I'm yelling")
I'm yelling!!!

>>> # or set a variable to what it returned
... yelling = shout("I'm yelling")
>>> yelling
"I'm yelling!!!"
>>> 

A few things to remember:
1. This function *returns* a string!  It does not print it.
2. You can test your function by calling it *after* you've defined it.
3. Remember... you can import your functions into an interactive Python session by using:

from shout import *

...if you started python in the same directory as your source file
"""
def shout(words):
	#print words,'!!!' # inserts a space btwn param & string
	#print words+'!!!'
	#print'%s!!!'%words
	return'%s!!!'%words