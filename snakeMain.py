import pygame, sys, random
from pygame.locals import *
from queue import *

pygame.init()

FPS = 30  # frames per second setting
SPEED = 200
fpsClock = pygame.time.Clock()

# time variable to determine if the snake's position has to update according to the SPEED variable
last = pygame.time.get_ticks()

# set up the window
DISPLAYSURF = pygame.display.set_mode((660, 480))
pygame.display.set_caption('Python!')

# set up the colors
BLACK       = (  0,       0,      0)
GREEN       = (  0,     255,      0)
RED         = (255,       0,      0)
YELLOW      = (255,     255,      0)
NAVYBLUE    = ( 60,      60,    100)

# draw the background on the surface object
DISPLAYSURF.fill(NAVYBLUE)

# snake x and y coordinates

snake = [(5, 5)] # snake head start position X = 5, Y = 5

# the apple's position
applePosX = random.randint(0, 10) * 60
applePosY = random.randint(0, 7) * 60

# All Directions
RIGHT = 'right'
LEFT = 'left'
DOWN = 'down'
UP = 'up'

# Queue that manages the input of the player (max size 2)
inputQueue = Queue(2)

# initial direction of the head
direction = RIGHT


# True if the two directions dir1 and dir2 are opposite
def opposite(dir1, dir2):
    if dir1 == RIGHT and dir2 == LEFT:
        return True
    elif dir1 == LEFT and dir2 == RIGHT:
        return True
    elif dir1 == UP and dir2 == DOWN:
        return True
    elif dir1 == DOWN and dir2 == UP:
        return True
    else:
        return False

# main game loop
while True:

    # for readability
    headPosX = snake[0][0]
    headPosY = snake[0][1]

    # draw background over the last frame
    DISPLAYSURF.fill(NAVYBLUE)

    # draw the apple
    pygame.draw.rect(DISPLAYSURF, RED, (applePosX, applePosY, 60, 60))

    # draw the snake's head
    pygame.draw.rect(DISPLAYSURF, YELLOW, (headPosX - 5, headPosY - 5, 60, 60))
    pygame.draw.rect(DISPLAYSURF, GREEN, (headPosX, headPosY, 50, 50))

    # what happens when the snake eats the apple
    if headPosX - 5 == applePosX and headPosY - 5 == applePosY:
        snake.append((snake[0][0], snake[0][1]))
        applePosX = random.randint(0, 10) * 60
        applePosY = random.randint(0, 7) * 60

    # draw the snake's tail
    for i in range(1, len(snake)):
        pygame.draw.rect(DISPLAYSURF, BLACK, (snake[i][0] - 5, snake[i][1] - 5, 60, 60))
        pygame.draw.rect(DISPLAYSURF, GREEN, (snake[i][0], snake[i][1], 50, 50))

    # get current time
    now = pygame.time.get_ticks()

    # has enough time passed since the last time request?
    if now - last >= SPEED:

        # processing the inputQueue
        if not inputQueue.empty():
            tmp = inputQueue.get()
            if not opposite(direction, tmp):
                direction = tmp;

        # moving the snake's tail accordingly
        for i in range(len(snake) - 1, 0, -1):
            snake[i] = snake[i - 1]

        # moving the snake's head according to it's direction
        if direction == RIGHT:
            headPosX += 60
            if headPosX >= 720:
                headPosX = 5

        elif direction == DOWN:
            headPosY += 60
            if headPosY >= 520:
                headPosY = 5

        elif direction == LEFT:
            headPosX -= 60
            if headPosX <= -55:
                headPosX = 605

        elif direction == UP:
            headPosY -= 60
            if headPosY <= -60:
                headPosY = 425

        # if the player hits one of the snakes tails the game is over
        for i in range(1, len(snake)):
            if snake[i][0] == headPosX and snake[i][1] == headPosY:
                pygame.quit()
                sys.exit()

        snake[0] = (headPosX, headPosY)

        # set the last time variable to 'now'
        last = now

    # process input from the player
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type == KEYUP and event.key == K_RIGHT:
            if inputQueue.full():
                inputQueue.queue.clear()
            else:
                inputQueue.put(RIGHT)
        elif event.type == KEYUP and event.key == K_LEFT:
            if inputQueue.full():
                inputQueue.queue.clear()
            else:
                inputQueue.put(LEFT)
        elif event.type == KEYUP and event.key == K_DOWN:
            if inputQueue.full():
                inputQueue.queue.clear()
            else:
                inputQueue.put(DOWN)
        elif event.type == KEYUP and event.key == K_UP:
            if inputQueue.full():
                inputQueue.queue.clear()
            else:
                inputQueue.put(UP)

    # display the frame and lock the FPS
    pygame.display.update()
    fpsClock.tick(FPS)
