import pygame
pygame.init()
WIDTH =600
HEIGHT =750
screen = pygame.display.set_mode((WIDTH,HEIGHT))

lighton = pygame.image.load("images\imageslightbulb\Image20260617163540.png")
lightoff = pygame.image.load("images\imageslightbulb\Image20260617163534.png")

lighton = pygame.transform.scale(lighton,(600,750))
lightoff = pygame.transform.scale(lightoff,(600,750))


while True :
    screen.fill("white")
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
    if event.type == pygame.MOUSEBUTTONDOWN :
        screen.blit(lighton,(0,0))
    else :
        screen.blit(lightoff,(0,0))    



    pygame.display.update()




