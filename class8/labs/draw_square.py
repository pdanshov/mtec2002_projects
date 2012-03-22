"""
draw_square.py
===
Draw a 100 x 100 square using the turtle module.

1. Bring in the turtle module using the import statement.
2. Draw a 100 by 100 square .  Hint: Combine turtle.forward and turtle.right (or turtle.left), and run them repeatedly.
3. Don't forget to put turtle.mainloop() at the end of your program!
4. (INTERMEDIATE) Make a funciton that draws a square.
	a. Write a function that takes 3 arguments: x, y and length... 
	b. This will place a length x length square at coordinates x, y.  
	c. Call it a few times using random coordinates and length.  
	d. Hint: Use up and goto 
	e. Hint: Make sure mainloop() is at the end of your program! 
"""

def square(x, y, length):
	import turtle
	turtle.up()
	turtle.goto(x-length/2, y-length/2)
	turtle.down()
	for x in range(4):
		turtle.forward(length)
		turtle.left(90)
	turtle.mainloop()