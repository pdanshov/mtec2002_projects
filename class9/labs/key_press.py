"""
key_press.py
===
Use the docs to handle a keyboard event:
http://www.pygame.org/docs/ref/event.html
http://www.pygame.org/docs/ref/key.html

When the user presses the spacebar, place the circle at a random position.
1. Create two variables, x and y... and initialize to where you want the circle to start
2. In the for event loop... check for: 
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
3. If that occurs, then change the value of x and y to random values
"""
import pygame
import random

FRAME_RATE = 30
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = "pdanshov"
x = WINDOW_WIDTH / 2
y = WINDOW_HEIGHT / 2

background_color = (100, 100, 0)
running = True
pygame.init()

screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
pygame.display.set_caption(WINDOW_TITLE)
clock = pygame.time.Clock()

pygame.key.set_repeat(10,10)
while running == True:

    # stop the main loop when window is closed 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            x = random.randint(0, WINDOW_WIDTH)
            y = random.randint(0, WINDOW_HEIGHT)
    screen.fill(background_color)

    # draw everything here!  this line draws a circle in the middle of the screen
    pygame.draw.ellipse(screen, (200,200,200), [315,100,100,255])
    pygame.draw.circle(screen, (0, 0, 200), (x ,y), 10)
    #rect = pygame.rect.Rect((25, 30), (50,60))
    pygame.draw.rect(screen, (200,200,200), [405,300,50,60])
    pygame.draw.arc(screen, (0,0,0), [500,300,100,200], 0, 0.8, 3)
    #pygame.gfxdraw.ellipse(screen, 25, 25, 50, 50, (200,200,200))
 
    clock.tick(FRAME_RATE)
    pygame.display.flip()

# exit when we're done with the loop
pygame.quit()
