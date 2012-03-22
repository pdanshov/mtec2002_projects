"""
chaining_functions.py
===
1. Create three functions named f1, f2 and f3
2. f1 will print "one"
3. f2 will call f1 and also print "two"
4. f3 will call f2 and also print "three"
5. print out "calling f1" and call f1; do the same for f3

Expected Output:
calling f1
one
calling f3
one
two
three
"""
def f1():
	print "one"
def f2():
	f1()
	print "two"
def f3():
	f2()
	print "three"
f3()