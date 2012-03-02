"""
Sum of Cubes
=====
* Create a list of ints using range, or create a list of ints using literals (range(10) or [1,2,3])... assign it to a variable named numbers
* Create a variable called sum_cubes and set it equal to 0
* Iterate through the numbers list using a for loop
* For every number, add the cube of that number to the variable sum_cubes
* Print out "Numbers: [your numbers list]"
* Print out "Sum Cubes: [your sum_cubes variables]"

Example Output:
Numbers: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Sum cubes: 2025
"""
numbers=range(10)
sum_cubes=0
for x in numbers:
    sum_cubes+=(x*x*x)
print 'Numbers: %r\nSum Cubes: %d'%(numbers,sum_cubes)