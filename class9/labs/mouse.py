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
import pygame

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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x = event.pos[0]
            y = event.pos[1]
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
