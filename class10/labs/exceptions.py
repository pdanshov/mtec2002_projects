"""
exceptions.py
=====
To handle errors, use a try/catch block:

-----
try:
	# do your stuff
except SomeError:
	# deal with some error
-----

optionally... you can continue catching more than one exception:

-----
.
.
except AnotherError:
	# deal with another error
-----

Substitute SomeError with the kind of error you want to handle - for example:

KeyError
ValueError
TypeError
IndexError
ZeroDivisionError
"""
#KeyError
d = {"shape":"circle"}
try:
	print d["shape"]
	print s["color"]
except KeyError:
	print "that key doesn't exist!!!!"
print "done"

#ValueError (conversion errors)
try:
	print int("this is not a number")
except ValueError:
	print "I don't think that's a number"
print "done"

#TypeError
try:
	print "foo" * "bar"
except TypeError:
	print "you can't multiply by that!"
print "done"

#IndexError
my_list = ["some", "stuff"]
try:
	print my_list[2]
except IndexError:
	print "that index is not in the mist"
print "done"

#ZeroDivisionError
try:
	5 / 0
except ZeroDivisionError:
	print "that's a no-no"
print "done"

#catching multiple possible exceptions - try possible KeyError AND TypeError like dictionary value divided by another value
#ex... which player do you want to add a score to, and add that score
d = {"score":10}
try:
	d["anything but score"] / 0
except KeyError:
	print "Key does not exist"
except ZeroDivisionError:
	print "Cannot divide by zero"