"""
myutils.py
===
1.  Create a function in this file (myutils) called shout(word) that returns the same word uppercased and with an exclamation point (search for the function that you would use to change case).
2.  Write doc tests in the doc string of the shout function.  In a multiline comment underneath the shout function definition, write out what the expected output of an interactive shell session.  For example: hello there would return HELLO THERE!
3.  Write in the code that runs the tests (see #7 and #8 in spanish.py).
4.  (Intermediate) Modify shout to take in another param, num, that adds that number of exclamation points to the word.
5.  (Intermediate) Adjust your tests accordingly.
6.  (Intermediate) Add another test that passes in two arguments - shout("hi", "foo"), but returns a default of one exclamation point when the second argument is not a number - 'HI!'
7.  (Intermediate) Run your program -- what happens?
8.  (Intermediate) Fix your program so that your new feature/test is implemented.  Implement it in whatever way you like (exception handling, checking if the argument is numeric, etc... for example: http://code.activestate.com/recipes/303495-check-that-a-string-represents-an-integer-number/)

"""
def shout(word, num):
	"""This is the doc test
	>>> shout("Hello There", 3)
	'HELLO THERE!!!'
	>>> shout("hi", "foo")
	'HI!'
	"""
	try:
		return "%s%s" % (word.upper(), "!"*num)
	except TypeError:
		return "%s!" % (word.upper())
if __name__ == "__main__":
	print shout("ciao", 13)
	import doctest
	doctest.testmod()