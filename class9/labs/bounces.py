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
6. (INTERMEDIATE) Try adding acceleration.  That is, on every bounce, change the velocity as well!
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
r = 10
x = WINDOW_WIDTH / 2
y = r
velocity_y = 3

while running == True:

    # stop the main loop when window is closed 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill(background_color)

    # draw everything here!  this line draws a circle in the middle of the screen
    pygame.draw.ellipse(screen, (200,200,200), [315,100,100,255])
    pygame.draw.circle(screen, (0, 0, 200), (x, y), r)
    #rect = pygame.rect.Rect((25, 30), (50,60))
    pygame.draw.rect(screen, (200,200,200), [405,300,50,60])
    pygame.draw.arc(screen, (0,0,0), [500,300,100,200], 0, 0.8, 3)
    #pygame.gfxdraw.ellipse(screen, 25, 25, 50, 50, (200,200,200))
    if (y>WINDOW_HEIGHT-r or y<0+r):
        velocity_y*=-2
    y+=velocity_y
    
    clock.tick(FRAME_RATE)
    pygame.display.flip()

# exit when we're done with the loop
pygame.quit()
