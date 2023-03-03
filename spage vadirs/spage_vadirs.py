import pygame
import random
pygame.init()
pygame.display.set_caption("spage vadirs!!!!!")
gamescreen = pygame.display.set_mode((800,800))
gameclock = pygame.time.Clock()
endgame = False
gamebgR = 40
gamebgG = 0
gamebgB = 30
pR = 240
pB = 240
pG = 240
pX = 400
pY = 750
leftward = False
rightward = False
notHittingWall = False
pWidth = 60
pHeight = 25
class Alien:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = xpos
        self.isAlive = True
    def draw(self):
        pygame.draw.rect(gamescreen, (250,250,250), (self.xpos, self.ypos, 40, 40))
while not endgame: # game loop -------------------------------------
 #https://docs.google.com/presentation/d/1Q1NO44sPD1N9lYssl-47hkM-ZbUspQ6bTZnWOZJtYDU/edit#slide=id.g1d61a57c6a2_0_40
    gameclock.tick(60) #gamespeed
    #input section
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            endgame = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                leftward = True
                print("going LEFT")
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                leftward = False
                print("left STOP")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                rightward = True
                print("going RIGHT")
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                rightward = False
                print("right STOP")
    #physics section

    if leftward == True and pX > 0:
        vX =-3
    if rightward == True and pX < 740:
        vX =+3
    if leftward == False and rightward == False:
        vX = 0
    #update p position
    pX += vX
    #some output things
    if pX <= 0:
        print("HIT LEFT BOUNDARY")
    if pX >= 740:
        print("HIT RIGHT BOUNDARY")
    #render section -------------------------------------------------
    a1 = Alien(400, 400)
    a1.draw()
    gamescreen.fill((gamebgR,gamebgG,gamebgB)) #wipe screen so it doesn't smear
    pygame.draw.rect(gamescreen, (pR, pG, pB), (pX, pY, pWidth, pHeight))
    pygame.draw.rect(gamescreen, (pR-10, pG-pG, pB-pB), (pX+20,pY-15,pWidth-40,pHeight+5))
    #pygame.draw.rect(gamescreen, (230, 0, 0), (420,735,20,30))
    pygame.display.flip()

#end game loop
pygame.quit