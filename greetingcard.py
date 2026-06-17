import pygame
import time
pygame.init()
WIDTH =600
HEIGHT =750
screen = pygame.display.set_mode((WIDTH,HEIGHT))

picture1 = pygame.image.load("images\Image20260617160552.jpg")
picture1 = pygame.transform.scale(picture1,(600,750))

picture2 = pygame.image.load("images\Image20260617160618.jpg")
picture2 = pygame.transform.scale(picture2,(200,200))

picture3 = pygame.image.load("images\Image20260617160557.jpg")
picture3 = pygame.transform.scale(picture3,(600,750))

font1 = pygame.font.SysFont("Sans Serif",50)
font2 = pygame.font.SysFont("Oswald",50)
while True :
    screen.fill("white")
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()

    screen.blit(picture1,(0,0))
    screen.blit(picture2,(300,375))

    text1 = font1.render("Happy birthday",True,"#c2380e")
    text2 = font2.render("Happy birthday",True,"#ffe100")

    screen.blit(text1,(175,300))
    
    

    pygame.display.update()

    time.sleep(2)
    screen.blit(picture3,(0,0))
    screen.blit(text2,(175,300))
    pygame.display.update()

    time.sleep(2)
    



    








