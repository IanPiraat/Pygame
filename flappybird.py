import pygame
pygame.init()
WIDTH =800
HEIGHT =700
screen = pygame.display.set_mode((WIDTH,HEIGHT))
background = pygame.image.load("images/imagesflappybird/Background.png")

ground = pygame.image.load("images/imagesflappybird/ground.png")
ground = pygame.transform.scale(ground,(1600,250))
groundx = 0

flappymiddle = pygame.image.load("images/imagesflappybird/bird2.png")
flappyup = pygame.image.load("images/imagesflappybird/bird3.png")
flappydown = pygame.image.load("images/imagesflappybird/bird1.png")

game = True
class bird(pygame.sprite.Sprite):
    def __init__(self, x, y,image,):
        super().__init__() 
        self.y = y
        self.x = x
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = self.x,self.y

        
        

flappy = bird(100,400,flappymiddle)

flappygroup = pygame.sprite.Group()
flappygroup.add(flappy)

class pipes(pygame.sprite.Sprite):
    def __init__(self,x,y,image,angle):
        super().__init__()
        self.x = x
        self.y = y
        self.image = image
        self.angle = angle
        self.rect = self.image.getrect()
        self.rect.center = self.x,self.y







while True :
    screen.fill("white")
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
    screen.blit(background,(0,0))
    screen.blit(ground,(groundx,600))
    if game == True :
        groundx -= .5
        if groundx < -450 :
            groundx = 0
    flappygroup.draw(screen)        
    pygame.display.update()





