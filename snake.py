import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 60 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Hello Pygame World!')

# set up the colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
RED = (255, 0, 0, 90)
GREEN = (0, 255, 0, 255)
BLUE = (0, 0, 255, 255)
NAVYBLUE = ( 60,  60, 100)

# draw on the surface object
DISPLAYSURF.fill(NAVYBLUE)

pygame.draw.rect(DISPLAYSURF, GREEN, (200, 150, 50, 50))

# snake x and y coordinates
headPosX = 5
headPosY = 5

# All Directions
RIGHT = 'right'
LEFT = 'left'
DOWN = 'down'
UP = 'up'

# direction of head
direction = RIGHT

# main game loop
while True:

    DISPLAYSURF.fill(NAVYBLUE)

    pygame.draw.rect(DISPLAYSURF, BLACK, (headPosX - 5, headPosY - 5, 60, 60))
    pygame.draw.rect(DISPLAYSURF, GREEN, (headPosX, headPosY, 50, 50))


    if direction == RIGHT:
        headPosX += 5
        if headPosX > 580:
            direction = DOWN

    elif direction == DOWN:
        headPosY += 5
        if headPosY > 420:
            direction = LEFT

    elif direction == LEFT:
        headPosX -= 5
        if headPosX < 10:
            direction = UP

    elif direction == UP:
        headPosY -= 5
        if headPosY < 10:
            direction = RIGHT


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)