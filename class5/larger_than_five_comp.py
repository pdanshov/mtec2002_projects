"""
Larger Than Five
=====
* Create a list of numbers from 0 through 9 using the range function, assign that to a variable called numbers
* Create an empty list called big_numbers
* Use a for loop to iterate through your numbers list...
* If the number is greater than five, append it to your big_numbers list
* Print "All numbers:"
* Print your numbers list
* Print "Big numbers:"
* Print your big_numbers list
* Use string interpolation or string concatenation for the above printing

Example Output:
All numbers: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Big numbers: [6, 7, 8, 9]
"""
numbers=range(10)
big_numbers=[x for x in numbers if x>5]
"""
for x in numbers:
    if x>5:
        big_numbers.append(x)
"""
print 'All numbers: %r \n'%numbers+'Big numbers: %(big)r'%{'big':big_numbers}