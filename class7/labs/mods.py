"""
mods.py
===
A module is just a text file with Python code in it.  Modules can be used to store reusable code, such as functions, classes.  You've actually used, and even created, modules before!  

You can use a module by importing it.  Here are a couple of ways of importing modules (one should look familiar to you!): 
* import my_module
* from my_module import *

Generally, it's best to use the "import my_module" style to preserve namespaces.  That is... if you import *, you can accidentally override code in the module or code that you've written.  When you import a moudle by using "my_module":
* a namespace is created with that module's name
* variables, functions and classes can be accessed in that module by using the module name and the dot (.) operator

Examples:
1. import math 				# importing a built-in module named math
2. print math.pi			# print out the variable named pi in the math module
3. x = math.ceil(3.7)		# call the function ceil() that's definited the math module; assign it to x

Python has many built-in modules.  We'll go over 3 of those modules in this file:
* random -  http://docs.python.org/library/math.html
	* random.randint(a, b) - returns a random number that greater than or equal to a and less than or equal to b
* math - http://docs.python.org/library/random.html
	* math.ceil(a) - returns the smallest integer value that's greater than or equal to a
	* math.sqrt(a) - returns the smallest integer value that's greater than or equal to a
* sys - http://docs.python.org/library/sys.html
	* sys.argv - a list of all of the "commandline" arguments
"""
# import the random, math and sys modules
import random
import math
import sys

### random
# create a list of mythical creatures, "unicorn", "dragon", and "yeti"... and assign it to a variable called creatures
creatures = ["unicorn", "dragon", "yeti"]

# create a random number using the randint function between 0 and 2, set it to a variable named index
index = random.randint(0, 2)

# print out index
print index

# ...now ...use the index to get an element from your list of creatures... print both the index and the creature out
print "%s, %s" % (index, creatures[index])

# do it again (set index and print out a creature from the list)
index = random.randint(0, 2)
print "%d, %s" % (index, creatures[index])

# and again (set index and print out a creature from the list)
index = random.randint(0, 2)
print "%r, %r" % (index, creatures[index])

def get_creature():
	creatures = ["unicorn", "dragon", "yeti"]
	index = random.randint(0, 2)
	print "%r, %r" % (index, creatures[index])

get_creature()

### math
# print out the closest integer that's greater that 7.8 using ceil
print math.ceil(7.8)

# get the squareroot of 17 using the sqrt function
print math.sqrt(17)

### sys
# print out the list of commandline arguments using argv
print sys.argv
print "%s" % sys.argv[1]
print "%s" % sys.argv[0]

# try running your file and adding a space and some text after your file name
"python mods.py added_arguement two three peter"