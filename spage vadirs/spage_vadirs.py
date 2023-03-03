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
pWidth = 60
pHeight = 25
while not endgame: # game loop -------------------------------------
    gameclock.tick(60) #gamespeed
    #input section
    for even in pygame.event.get():
        #https://docs.google.com/presentation/d/1Q1NO44sPD1N9lYssl-47hkM-ZbUspQ6bTZnWOZJtYDU/edit#slide=id.g1d61a57c6a2_0_40
        print("nothing here yet")
    #physics section

    if leftward == True:
        vx =-3
    else:
        vx = 0
    #update p position
    pX += vx
    #render section -------------------------------------------------
    
    gamescreen.fill((gamebgR,gamebgG,gamebgB)) #wipe screen so it doesn't smear
    pygame.draw.rect(gamescreen, (pR, pG, pB), (pX, pY, pWidth, pHeight))
    pygame.draw.rect(gamescreen, (pR-10, pG-pG, pB-pB), (pX+20,pY-15,pWidth-40,pHeight+5))
    #pygame.draw.rect(gamescreen, (230, 0, 0), (420,735,20,30))
    pygame.display.flip()

#end game loop
pygame.quit