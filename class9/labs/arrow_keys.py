"""
arrow_keys.py
===
Use the docs to handle keyboard events:
http://www.pygame.org/docs/ref/event.html
http://www.pygame.org/docs/ref/key.html

When the user presses an arrow key, move the circle appropriately
1. Create two variables, x and y... and initialize to where you want the circle to start
2. Add this line right before the while loop:  pygame.key.set_repeat(10,10)
3. In the for event loop... check for the arrow keys.  See the reference above.  You can continue using elifs: 
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
4. If that occurs, then change the y or x value appropriately (up means decrement y, down means increment y, etc)
"""
