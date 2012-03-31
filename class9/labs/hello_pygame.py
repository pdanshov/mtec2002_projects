"""
hello_pygame.py
===
PyGame is a module that provides access to audio, keyboard, mouse, joystick and 2D and 3D graphics.  It's used for creating animations, interactive programs, and - of course - games.

1. Unlike turtle, PyGame's coordinate system starts with the origin, (0, 0), on the upper left hand corner.
2. The x and y axis goes up as you travel right and down.

Use this file as a template for future pygame projects.  This boilerplate code consists of several parts:
1. Setup code that gets run once.  This is everything before the while loop (which loops forever, until window close).  Think of this as setup() in processing.
2. Code that gets run repeatedly.  This is everything within the while loop.  Think of this as loop() in processing.
3. Code that checks for events.  This happens once in every iteration of the while loop.

Try changing the following parts of this program:
1. background
2. window title
3. frame rate
4. window width
5. window height
4. draw a rectangle, ellipse and arc using the documentation: http://www.pygame.org/docs/ref/draw.html
"""
import pygame

FRAME_RATE = 30
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = "pdanshov"

background_color = (100, 100, 0)
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

    # draw everything here!  this line draws a circle in the middle of the screen
    pygame.draw.ellipse(screen, (200,200,200), [315,100,100,255])
    pygame.draw.circle(screen, (0, 0, 200), (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), 10)
    #rect = pygame.rect.Rect((25, 30), (50,60))
    pygame.draw.rect(screen, (200,200,200), [405,300,50,60])
    pygame.draw.arc(screen, (0,0,0), [500,300,100,200], 0, 0.8, 3)
    #pygame.gfxdraw.ellipse(screen, 25, 25, 50, 50, (200,200,200))
 
    clock.tick(FRAME_RATE)
    pygame.display.flip()

# exit when we're done with the loop
pygame.quit()
