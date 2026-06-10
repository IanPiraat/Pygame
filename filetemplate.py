import pygame
pygame.init()
WIDTH =500
HEIGHT =500
screen = pygame.display.set_mode((WIDTH,HEIGHT))


while True :
    screen.fill("white")
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()


    pygame.display.update()




