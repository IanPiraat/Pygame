import pygame
pygame.init()
WIDTH = 960
HEIGHT =549
playercharge = False
screen = pygame.display.set_mode((WIDTH,HEIGHT))

background = pygame.image.load("images/images probow/bg.png")
playeridle = pygame.image.load("images/images probow/playeridle.png")
playercharge = pygame.image.load("images/images probow/playercharge.png")
background  = pygame.transform.scale(background,(960,549))
arrow = pygame.image.load("images/images probow/arrow.png")
arrow = pygame.transform.scale(arrow,(50,50))
class player(pygame.sprite.Sprite) :
    def __init__(self,x,y,health,image,status):
        super().__init__()
        
        self.x = x
        self.y = y 
        self.status = status
        self.health = health
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        
class arrows(pygame.sprite.Sprite) :
    def __init__(self,x,y,image,velocity,charge,damage) :
        super().__init__()
    
        self.x = x 
        self.y = y
        self.image = image 
        self.velocity = velocity
        self.charge = charge
        self.damage = damage
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        
player1 = player(100,400,health=100,image=playeridle,status="idle",)
arrow1 =  arrows(player1.x,player1.y,image=arrow,velocity=5,charge=100,damage=10)      
    
playergroup = pygame.sprite.Group()
arrowgroup = pygame.sprite.Group()
playergroup.add(player1)
arrowgroup.add(arrow1)








while True :
    screen.fill("white")
    screen.blit(background,(0,0))
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
    arrowgroup.draw(screen)
    playergroup.draw(screen)

    pygame.display.update()




