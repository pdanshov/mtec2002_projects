"""
Input Cubed
=====
* Use the function you created in cubes_function.py in a program that retrieves user input.  
* Import all functions from the cube_function.py so that you don't have to rewrite the code
	* Write this program in the same directory as cube_function.py, and run it from the same directory.  
	* Remember, to import, use the from .... import * 
* The user input will be a comma delimited string, such as "1,2,3".  
* Hint: Create a helper function that turns a string into a list of ints (remember, you can use int() to cast a string into an integer)

Example Output:
Gimmeh string of numberz, commas separated plz... 1,2,3
[1, 8, 27]
"""
def helper(s):
    return[int(x) for x in s.split(',')]
from cubes_func import*
print 'Gimmeh string of numberz, commas separated plz...',cube(helper(raw_input('')))