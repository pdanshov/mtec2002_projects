"""
divisible_by_twelve.py
===
1. Ask the user (print out) for a number that's divisible by 12
2. Prompt the user for input, and store the input in a variable called num
3. Use a while loop to continue to ask the user for input until the user gives a number that's divisible by 12

Hints:
1. Use the modulo operator to determine if num is divisible by twelve
2. Use int to convert the user's input from a string to an int

Example Output:
Give me a number that's divisible by 12
>65
Give me a number that's divisible by 12
>29
Give me a number that's divisible by 12
>144
Thanks! 144 is divisible by 12
"""

num=None
while num==None or num%12!=0:
	num=int(raw_input('Give me a number that\'s divisible by twelve \n > '))
print'%d is divisible by twelve!'%num