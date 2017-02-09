import pygame


class snake:

    __snake = []

    def __init__(self, headPosX, headPosY):
        self.__snake.append((headPosX, headPosY))

    def drawSnake(self, displaysurfaces):

        # draw the snake's head
        pygame.draw.rect(displaysurfaces, (255, 255, 0), (self.getHeadPosX() - 5, self.getHeadPosY() - 5, 60, 60))
        pygame.draw.rect(displaysurfaces, (0, 255, 0), (self.getHeadPosX(), self.getHeadPosY(), 50, 50))

        # draw the tail
        for i in range(1, len(self.__snake)):
            pygame.draw.rect(displaysurfaces, (0, 0, 0), (self.__snake[i][0] - 5, self.__snake[i][1] - 5, 60, 60))
            pygame.draw.rect(displaysurfaces, (0, 255, 0), (self.__snake[i][0], self.__snake[i][1], 50, 50))

    def collides(self):
        for i in range(1, len(snake)):
            if snake[i][0] == self.getHeadPosX() and snake[i][1] == self.getHeadPosY():
                return True
        return False

    def addSnakePart(self):
        self.__snake.append((self.__snake[-1][0], self.__snake[-1][1]))

    def getHeadPosX(self):
        return self.__snake[0][0]

    def getHeadPosY(self):
        return self.__snake[0][1]

    def getTail(self):
        return self.__snake.pop(0)


