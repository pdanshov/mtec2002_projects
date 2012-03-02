"""
Hotness
=====
Write a function called f_to_c.  It should take one parameter, called temperature, as an input - the temperature in Fahrenheit.  The function should return the temperature in Celsius.  The formula to convert Fahrenheit to Celsius is:

C = 5/9 (F-32)

Example Output (after importing into Python interactive shell):

>>> from hotness import *
>>> f_to_c(44.8)
7.11111111111111
>>> f_to_c(32)
0.0
"""

def f_to_c(temp):
	c=round((temp-32.0)/1.8,0)
	return c
print f_to_c(98.6)