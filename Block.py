import pygame as pg

class Block:
    def __init__(self, screen, colour, xconst, width, height):
        self.screen = screen
        self.colour = colour
        self.xconst = xconst
        self.width = width
        self.height = height

        self.wWidth, self.wHeight = pg.display.get_surface().get_size()
        self.y = self.wHeight // 2

    def draw(self):
        self.updateY()
        if self.y <= 0:
            self.y = 0
        elif (self.y + self.height) >= self.wHeight:
            self.y = self.wHeight - self.height
        pg.draw.rect(self.screen, self.colour, [self.xconst, self.y, self.width, self.height])

    def updateY(self):
        pass

    def getSize(self):
        return (self.xconst, self.y, self.width, self.height)


class PlayerBlock(Block):
    def __init__(self, screen, colour, xconst, width, height):
        super().__init__(screen, colour, xconst, width, height)

    def updateY(self):
        self.y = pg.mouse.get_pos()[1]


class NPC_Block(Block):
    def __init__(self, screen, colour, xconst, width, height, speed, ball):
        super().__init__(screen, colour, xconst, width, height)
        self.speed = speed
        self.followBall = ball
        self.middle = self.y + (self.height / 2)

    def updateY(self):
        self.middle = self.y + (self.height / 2)
        newY = self.followBall.getPos()[1]
        direction = (newY - self.middle)
        self.y += direction
