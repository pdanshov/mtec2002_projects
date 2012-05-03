"""
spanish.py
===
1.  Create a function to_spanish(word) that translate dog and cat to perro and gato using a dictionary.
2.  Test your function by calling the function after your function definition... and printing out the result.
3.  Find translate.py; it's in the same directory as this file. 
4.  In translate.py, import this (spanish) module.
5.  In translate.py, call the to_spanish function in this (spanish) module on 'cat' and print out the result.
6.  Try running translate.py.  What is printed out?  Why?
7.  Use if __name__ == "__main__": to prevent code from being run when imported as a module.
8.  Use doctests by writing what you expect in your comments, and then adding the following lines within your check for main:
	import doctest
	doctest.testmod()
9.  Note that you don't need to use the module name as a prefix in the doctest comment.
10. Modify translate.py to accept a single argument on the commandline... and pass that argument on to the function call:
	import sys
	...
	# use sys.argv[1] to get the first item passed in through the commandline
"""
def to_spanish(anything):
	"""This function translates stuff to spanish
	>>> to_spanish("cat")
	'gatto'
	>>> to_spanish("hello")
	'hola'
	"""
	translation = {"cat":"gatto", "dog":"perro"}
	return translation[anything]	
	"""if anything == "cat":
		return "gatto"
	"""
# only run the test if this is the script that's being run
#print to_spanish("cat")
#print __name__
if __name__ == "__main__":
	print to_spanish("cat")
	import doctest
	doctest.testmod()