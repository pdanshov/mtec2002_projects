"""
confused_turtle.py
===
1. Bring in the turtle module using the import statement.
2. Bring in the random module using the import statement.
3. Write a for loop that loops 100 times by using the range function.
4. For each iteration of the loop
	a. create a variable called my_x and set it to a random integer between -150 and 150 using random.randint(-150, 150)
	b. create a variable called my_y and set it to a random integer between -150 and 150 using random.randint(-150, 150)
	c. call turtle.goto(x,y)  
"""
import turtle
import random
for x in range(100):
	my_x = random.randint(-150, 150)
	my_y = random.randint(-150, 150)
	turtle.goto(my_x, my_y)