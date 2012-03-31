"""
random_animation.py
===
In addition to moving from top to bottom, add some random lateral motion by adjusting the circle's velocity.

Rewrite the top to bottom animation code:
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

Add random lateral motion (that is, animate along the x-axis):
1. Before the while loop, add a velocity_x variable and set it to 0
2. Within the while loop, change the velocity_x variable to a random integer value between -1 and 1
3. Add the new velocity to x
4. Run the program to see what happens
5. Bound the velocity to a value between -2 and 2 using a conditional for a less pronounced effect
"""
import pygame
import random

FRAME_RATE = 30
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = "My Game"

background_color = (45, 45, 45)
running = True
pygame.init()

screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
pygame.display.set_caption(WINDOW_TITLE)
clock = pygame.time.Clock()
x = WINDOW_WIDTH / 2
y = 0
velocity_y = 1
velocity_x = 00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

while running == True:

    # stop the main loop when window is closed 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill(background_color)

    # draw everything here!  this line draws a circle in the middle of the screen
    pygame.draw.circle(screen, (200, 200, 200), (x, y), 10)
    pygame.draw.circle(screen, (205, 140, 149), (x, y), 6)
    y += velocity_y
    velocity_x = random.randint(-1, 1)
    x += velocity_x

    if y >= WINDOW_HEIGHT:
        y = 0
        
    clock.tick(FRAME_RATE)
    pygame.display.flip()

# exit when we're done with the loop
pygame.quit()
