"""
bounces.py
===
Animate the circle so that it moves from top to bottom.  When it hits the bottom, it should reverse its direction.  This can be done by multiplying the velocity by -1 to flip the sign of the velocity.
1. Copy the boilerplate code from the template exercise - hello_pygame.py.
2. Create the following variables:
	a. create a variable named r and set it equal to the radius of the circle; let's use 10
	b. create a variable to store the circle's x coordinate; call it x and set it equal to half of the window's width
	c. create a variable to store the circle's y coordinate; call it y and set it equal to the radius (which was the variable r that we defined above)
	d. create a variable to store the circle's velocity along the y axis and set it equal to 3
3. In the main loop, check if y is greater than the height of the screen minus the radius.  
4. If it's greater, then multiply the velocity by -1 to flip the velocity.
5. Do the same check for the top of the screen... that is, if the y position is less than 0 plus the radius.
6. (INTERMEDIATE) Try adding acceleration.  That is, on every bounce, change the velocity as well!  When it bounces, dampen the velocity by dividing it by some small value AND changing the sign.  velocity_y = int(velocity_y / -1.3)
"""
