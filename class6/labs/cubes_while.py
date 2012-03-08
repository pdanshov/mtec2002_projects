"""
cubes_while.py
===
1. Create a list of numbers 0 through 9 using the range function; assign it to a variable named numbers
2. Create an empty list called cubes
3. Using a while loop and a counter variable, iterate through all of the numbers in the original list
4. Append the cube of the number to the cubes list

Example Output:
List of numbers: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
List of cubes: [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
"""
numbers=range(10)
cubes=[]
count=0
while count<len(numbers):
	cubes.append((count**3))
	count+=1
print numbers
print cubes