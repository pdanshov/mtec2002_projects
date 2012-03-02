"""
Sum
=====
* Create a list of ints using range, or create a list of ints using literals (range(10) or [1,2,3])... assign it to a variable named numbers
* Create a variable called total and set it equal to 0
* Iterate through the numbers list using a for loop
* For every number, add it to the variable total
* Print out "Numbers: [your numbers list]"
* Print out "Sum: total"
* There's already a function that does this!  Can you guess what it is?

Example Output:
Numbers: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Sum: 45

"""
numbers=range(10)
total=0
for x in numbers:
    total+=x
print 'Numbers: %r\nSum: %d'%(numbers,total)
print sum(range(10))