import pygame as pg
import Block
import Ball

pg.init()


def init():
    global ball, player, opp, blocks, blockSizes
    ball = Ball.Ball(screen, colours["WHITE"], 5, ballSpeed)
    #player = Block.PlayerBlock(screen, colours["WHITE"], blockWidth, blockWidth, blockHeight)
    opp = Block.NPC_Block(screen, colours["WHITE"], (sWidth - blockWidth * 2), blockWidth, blockHeight, blockSpeed, ball)
    opp2 = Block.NPC_Block(screen, colours["WHITE"], blockWidth, blockWidth, blockHeight, blockSpeed, ball)

    #blocks = [player, opp]
    blocks = [opp, opp2]
    blockSizes = []

colours = {
    "WHITE": (255,255,255),
    "BLACK": (0,0,0)
}

blockSpeed = 10
ballSpeed = 50

sWidth = 700
sHeight = 500

blockWidth = 10
blockHeight = 50

screen = pg.display.set_mode((sWidth, sHeight))
pg.display.set_caption("Pong")
done = False
clock = pg.time.Clock()
pg.mouse.set_visible(False)
init()

while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    screen.fill(colours["BLACK"])

    ball.draw(blockSizes)
    blockSizes = []
    for block in blocks:
        blockSizes.append(block.getSize())
        block.draw()

    ballPosX = ball.getPos()[0]
    if ballPosX <= 0 or ballPosX >= sWidth:
        init()

    pg.display.flip()
    clock.tick(120)

pg.quit()
