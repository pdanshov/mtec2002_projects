"""
Heavy
=====
Write a function called lb_to_kg.  It should take one parameter, called weight, as an input - a weight in pounds.  The function should return the weight in kilograms.  The formula to convert pounds to kilograms is:

kg = lb/2.2

Example Output (after importing into Python interactive shell):
>>> from heavy import *
>>> lb_to_kg(100)
45.45454545454545

Extra Credit #1 - What happens if you don't pass in a number?  How can you clean the input or prevent an error from occurring if a string is passed in rather than a number?  Implement it.
"""
"""
def lb_to_kg(weight):
	kg = weight/2.2
print kg
#the above will say 'kg not defined'
"""

def lb_to_kg(weight):
    try:
        var=int(weight)
        print 'Is an integer'
        kg=round(weight/2.2,0)
        print kg
    except (TypeError, ValueError, NameError):
        print 'Not an integer'