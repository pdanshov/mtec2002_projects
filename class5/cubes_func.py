"""
Cubes
=====
Convert cubes.py into a function called cube that takes a list and returns a list of cubes.

Example Output (if imported into interactive shell):
>>> from cubes_func import *
>>> cube([1,2,3])
[1, 8, 27]
"""
def cube(list):
    cubes=[]
    for x in list:
        cubes.append(x*x*x)
    return cubes