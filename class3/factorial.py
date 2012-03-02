"""
Factorial
=====

This is a classic recursion problem.  Without looking up the solution, create a function that calculates the factorial of a number.  The factorial of n is the product of all of the positive integers that are less than or equal to n:  

n! = n * (n - 1)! for n > 0
n! = 1 for n = 0

For a more concrete example, see 4 factorial:

4! = 4 * 3 * 2 * 1

Note that 0! = 1

Without using loops, can you come up with a way to calculate factorial?  Hint: you can call the function that you just defined in your function definition!  So... you could do something like:

def foo():
	return foo()

Of course, that would continue going on forever.  You would have to put some guard condition to stop the execution of the program.  The guard condition for factorial is related to the fact that 0! = 1.

Example Output (after importing into Python interactive shell):
>>> from factorial import *
>>> fact(0)
1
>>> fact(1)
1
>>> fact(2)
2
>>> fact(3)
6
>>> fact(4)
24
>>> fact(5)
120

Want to cheat?  See http://www.openbookproject.net/thinkcs/python/english2e/ch11.html, sections 11.8 and 11.9.
"""
"""
def fact(n):
    if n==0 or n==1:
        print'1'
    else:
        f=n*(n-1)
        print f
"""
"""
def fact(n):
    if n>1:
        n=n*(n-1)
        print '1 or 0'
        return fact(n)
    elif n==0 or n==1:
        print '1'
    else:
        print 'f'
"""

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
        
def fibonacci(n):
    if n==0 or n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
