"""
screen_wrap.py
===
Move the circle from top to bottom, but when it reaches the bottom, change the circle's x and y coordinates so that it starts at the top again.

1. Copy the boilerplate code from the template exercise - hello_pygame.py.
2. Rewrite the top to bottom animation code.
3. Write a conditional in the while loop that checks if the circle is at the bottom of the screen.
4. Make the radius of the circle into a variable, and use it to augment your boundary conditions for the bottom of the screen
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
    if y>=WINDOW_HEIGHT:
        y=0
    
    clock.tick(FRAME_RATE)
    pygame.display.flip()

# exit when we're done with the loop
pygame.quit()