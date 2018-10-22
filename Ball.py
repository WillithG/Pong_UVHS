import pygame as pg
import math
import random

"""
    implement a better way to detect collision:
    - more general
    - more intuitive and straightforward way to determine how to bounce
"""
class Ball:
    def __init__(self, screen, colour, size, speed):
        self.screen = screen
        self.colour = colour
        self.size = size
        self.speed = speed

        self.wWidth, self.wHeight = pg.display.get_surface().get_size()
        self.x = 0
        self.y = 0
        self.angle = 0
        self.initVel()

        self.centre = (self.x) + self.size / 2
        self.radius = self.size / 2
        self.MAX_BOUNCE_ANGLE = -math.radians(75)
        self.xCoeff = 1
        self.yCoeff = 1

    def initVel(self):
        self.wWidth, self.wHeight = pg.display.get_surface().get_size()
        self.x = self.wWidth // 2
        self.y = self.wHeight // 2

        direc = random.randint(0,1)
        CONE_ANGLE = 75
        INC_ANGLE = -0.5*math.pi + (math.pi - math.radians(CONE_ANGLE))/2
        # left
        if direc == 0:
            initCone = math.pi + INC_ANGLE
        # right
        else:
            initCone = INC_ANGLE
        randCone = random.random() * math.radians(CONE_ANGLE)
        self.angle = initCone + randCone

    def move(self, blockSizes):
        self.x += self.speed * self.xCoeff * math.cos(self.angle)
        self.y += self.speed * self.yCoeff * math.sin(self.angle)

        self.centre = (self.x) + self.size / 2
        # reflection if it hits the edge of screen
        if self.y >= self.wHeight or self.y <= 0:
            self.yCoeff *= -1
        elif self.detectCollision(blockSizes):
            self.bounce()

    # MAKE THIS BETTER
    def bounce(self):
        bY = self.collY
        bHeight = self.collHeight
        relativeYIsect = (bY + (bHeight/2)) - self.y
        normalised = (relativeYIsect/(bHeight/2))
        self.xCoeff *= -1
        self.angle = normalised * self.MAX_BOUNCE_ANGLE

    def detectCollision(self, blockSizes):
        for block in blockSizes:
            xconst = block[0]
            bY = block[1]
            bWidth = block[2]
            bHeight = block[3]

            rBlockColl = abs((xconst + bWidth) - self.centre) <= self.radius
            lBlockColl = abs(xconst - self.centre) <= self.radius
            withinY = self.y >= bY and self.y <= (bY + bHeight)

            if withinY and (rBlockColl or lBlockColl):
                self.collY = bY
                self.collHeight = bHeight
                return True

    def draw(self, blockSizes):
        self.move(blockSizes)
        pg.draw.ellipse(self.screen, self.colour, [self.x, self.y, self.size, self.size])

    def getPos(self):
        self.middleX = (self.x) + self.size / 2
        self.middleY = self.y + (self.size / 2)
        return self.middleX, self.middleY
