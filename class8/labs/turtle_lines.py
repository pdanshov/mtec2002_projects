""" turtle_lines.py === Experiment with the built in turtle module.  The turtle
module allows you to work with a "virtual pen plotter".

See http://docs.python.org/release/3.1.3/library/turtle.html

1. The turtle (pen) can be up or down.  When it's down, it draws a line
wherever the turtle moves. 2. The center of the window, the origin, is at (0,
0) 3. You will have to tab over to the window that creates your program since
it may not have focus when you first run it 4. Terminal will "wait" until you
quit the program... so you have to close the window that the program creates to
end the program

Some commands that you can use: 1. turtle.up() 			# pick up the turtle
(pen), don't draw 2. turtle.down() 		# put down the turtle (pen), draw 3.
turtle.right(90) 	# turn the turtle right 90 degrees 4. turtle.left(180)
	# turn the turtle left 180 degrees 5. turtle.forward(100) 	# move the
turtle fowards 100 pixels 6. turtle.goto(0, 0) 	# move hte turtle to the
coordinates (0, 0) 7. turtle.mainloop() 	# *always* call this at the end of
your program to start the main even loop """

# use the import statement to bring in the turtle module
import turtle

# use the import statement to bring in the random module
import random

# move the turtle foward 100 pixels
turtle.forward(100)

# turn the turtle 90 degrees to the left
turtle.left(90)

# move the turtle foward by a random number - between 5 and 20 - of pixels
turtle.forward(random.randint(5, 20))

# pick up the pen
turtle.up()

# move the turtle foward by a random number - between 5 and 20 - of pixels
turtle.forward(random.randint(5, 20))

# put the pen back down
turtle.down()

# use a for loop to repeat the previous 4 lines 7 times
for x in range(7):
	turtle.forward(random.randint(5, 20))
	turtle.up()
	turtle.forward(random.randint(5, 20))
	turtle.down()
	
# use the goto method to move to the coordinate (-50, -100)
turtle.goto(-50, -100)

# start the main event loop (see #7)
turtle.mainloop()