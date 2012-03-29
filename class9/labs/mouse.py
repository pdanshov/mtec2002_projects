"""
mouse.py
===
Use the docs to handle mouse events:
http://www.pygame.org/docs/ref/event.html

1. event.pos has a tuple containing the mouse coordinates; index 0 is x, index 1 is y
2. The event type for mouse button down is pygame.MOUSEBUTTONDOWN

When the user presses a mouse button place the circle at those x and y coordinates:
1. Create two variables, x and y... and initialize to where you want the circle to start
2. In the for event loop... check for the a mouse button down event.  See the reference above. 
3. If that occurs, then change y or x value to the event's x or y value
"""
