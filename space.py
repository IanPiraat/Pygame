import pygame
pygame.init()
WIDTH =1600
HEIGHT =1000
screen = pygame.display.set_mode((WIDTH,HEIGHT))
p_space = pygame.image.load("images\imagespace\Image20260617164523.png")
p_space = pygame.transform.scale(p_space,(1600,1000))

p_player1 = pygame.image.load("images\imagespace\Image20260617164516.png")
p_player1 = pygame.transform.scale(p_player1,(500,413))

p_player2 = pygame.image.load("images\imagespace\Image20260617164520.png")
p_player2 = pygame.transform.scale(p_player2,(500,413))

while True :
    screen.fill("white")
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
    screen.blit(p_space,(0,0))

    screen.blit(p_player1,(50,200))

    screen.blit(p_player2,(600,1400))


    pygame.display.update()




