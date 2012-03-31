"""
winter_scene.py
===
Using the drawing and animation techniques we learned create an animation of snow falling.

1. Copy the boilerplate code from the template exercise - hello_pygame.py.
2. Incorporate the code from multiple_objects.py to create the snow:
	a. However, in the setup, rather than use 0 for the initial y value, use a random value
	b. In the main loop, when iterating over the circles, check if the y value is greater than the window width (see screen_wrap.py)
	c. If the y value is greater... then bring the circle back up to the top
3. (INTERMEDIATE) Incorporate random lateral motion.  Try adding a unique velocity for x and y for each circle by expanding your two element list!  You can also use a dictionary if it makes more sense than a list with indexes.

"""
import pygame
import random

FRAME_RATE = 30
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Winter Scene"
NUM_CIRCLES = 75
circles = []
r = 10
r2 = 3

for c in range(NUM_CIRCLES):
    circles.append([random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT), random.randint(1,3), random.randint(-2,1)])
print circles

background_color = (75,75,75)
running = True
pygame.init()

screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
pygame.display.set_caption(WINDOW_TITLE)
clock = pygame.time.Clock()

while running == True:

    # stop the main loop when window is closed 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill(background_color)
    # draw here

    for c in circles:
        pygame.draw.ellipse(screen, (255,255,255), [c[0],c[1],r,10])
        pygame.draw.ellipse(screen, (145,145,145), [c[0],c[1],r2,3])
        #pygame.draw.circle(screen, (200, 200, 200), (c[0], c[1]), 10)
        #pygame.draw.circle(screen, (205, 140, 149), (c[0], c[1]), 6)
        c[1] += c[2] #velocity_y
        if (c[1] >= WINDOW_HEIGHT):
            c[1] = 0
        elif (c[0] >= WINDOW_WIDTH or c[0] <= 0):
            c[1] = -5
            c[0] = random.randint(WINDOW_WIDTH/5, WINDOW_WIDTH)
    
    clock.tick(FRAME_RATE)
    pygame.display.flip()
