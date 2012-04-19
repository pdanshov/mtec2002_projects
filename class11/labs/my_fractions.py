"""
fractions.py
=====
Create a class called Fraction that represents a numerator and denominator.
Implement the following methods:

1. __init__ with self, numerator and denominator as arguments that sets a numerator and denominator attribute
2. __str__ with self as the only argument... that prints out a fraction as numerator/denominator ...for example, 1/2
3. pretty_print with self as the only argument... it prints out:
	1
	-
	2
4. multiply with self and another Fraction as the arguments... it should alter the numerator and denominator of the current fraction, but it's not necessary to reduce
5. (INTERMEDIATE) add with self and another Fraction as the arguments... it should alter the numerator and denominator of the currecnt fraction, but it's not necessary to reduce

Some example output from the interactive shell:
>>> a = Fraction(1,2)
>>> print a
1/2
>>> a.pretty_print()
1
-
2
>>> a.add(Fraction(1,4))
>>> print a
6/8
>>> a.multiply(Fraction(2,3))
>>> print a
12/24
>>> 
"""
