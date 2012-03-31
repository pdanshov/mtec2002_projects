"""
simple_animation.py
===
In this exercise, we'll animate a circle so that it moves from the top of the screen to the bottom of the screen...

1. We'll store the circle's coordinates and velocity in the variables x, y and velocity.  
2. Since our game loops continuously, if we redraw the circle at a different position after each iteration of the loop, it will look like it's moving.  
3. To do this, we'll draw the circle using the values of x and y as the coordinates.  
4. At each iteration, we'll also increment that position with the value that we have in the velocity variable.

To write this code:
1. Copy the boilerplate code from the template exercise - hello_pygame.py.
2. Create three variables above the for loop.  Name them x, y and velocity_y.  Set them to the following values: 
	x: window_dimensions[0] / 2
	y: 0
	velocity_y: 1
3. Draw a circle using the x and y values above
	a. The code for the circle should go after the line that fills the background color in the while loop.  
	b. Use the x and y values to set the coordinates of the circle.
	c. Use the docs if you need help with calling the function: http://www.pygame.org/docs/ref/draw.html#pygame.draw.circle
4. Increment your y value by adding velocity_y.
"""
import pygame

FRAME_RATE = 30
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = "My Game"

background_color = (100, 100, 0)
running = True
pygame.init()

screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
pygame.display.set_caption(WINDOW_TITLE)
clock = pygame.time.Clock()
x = WINDOW_WIDTH / 2
y = 0
velocity_y = 6

while running == True:

    # stop the main loop when window is closed 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill(background_color)

    # draw everything here!  this line draws a circle in the middle of the screen
    pygame.draw.ellipse(screen, (200,200,200), [315,100,100,255])
    pygame.draw.circle(screen, (0, 0, 200), (x, y), 10)
    #rect = pygame.rect.Rect((25, 30), (50,60))
    pygame.draw.rect(screen, (200,200,200), [405,300,50,60])
    pygame.draw.arc(screen, (0,0,0), [500,300,100,200], 0, 0.8, 3)
    #pygame.gfxdraw.ellipse(screen, 25, 25, 50, 50, (200,200,200))
    
    y+=velocity_y
    
    clock.tick(FRAME_RATE)
    pygame.display.flip()

# exit when we're done with the loop
pygame.quit()