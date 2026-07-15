
import random
import pygame
pygame.init()
WIDTH =500
HEIGHT =500
score1 = 0
score2 = 0 
screen = pygame.display.set_mode((WIDTH,HEIGHT))
player_image = pygame.image.load("images/images 2player!/pirate/pirate.png")
player_image = pygame.transform.scale(player_image,(75,75))

player_image2 = pygame.image.load("images/images 2player!/pirate/parrot.png")
player_image2 = pygame.transform.scale(player_image2,(75,75))

collectible_image = pygame.image.load("images\images 2player!\pirate\damage.png")
collectible_image = pygame.transform.scale(collectible_image,(75,75))")


playergroup = pygame.sprite.Group() 
collectiblegroup = pygame.sprite.Group()


font = pygame.font.SysFont("Arial",24)

class payer1(pygame.sprite.Sprite) :
    def __init__(self,x,y,image):
        super().__init__()
        self.x = x
        self.y = y
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = self.x,self.y
    def update(self,k) :
        
        if k[pygame.K_UP]:
                self.rect.y -= 1
        if k[pygame.K_DOWN] :
                self.rect.y += 1
        if k[pygame.K_RIGHT] :
                self.rect.x += 1
        if k[pygame.K_LEFT] :
                self.rect.x -= 1
                
class payer2(pygame.sprite.Sprite) :
    def __init__(self,x,y,image):
        super().__init__()
        self.x = x
        self.y = y
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = self.x,self.y
        

    def update(self,k)  :
            if k[pygame.K_w]:
                self.rect.y -= 1
                
            if k[pygame.K_s]:
                self.rect.y += 1
                
            if k[pygame.K_d]:
                self.rect.x += 1
                
            if k[pygame.K_a]:
                self.rect.x -= 1
                
class collectible(pygame.sprite.Sprite) :
    def __init__(self,x,y,image):
            super().__init__()   
            self.x = x
            self.y = y
            self.image = image      




player1 = payer1(175,250,player_image)
player2 = payer2(175,300,player_image2)

collectible = 
player1.add(playergroup)

player2.add(collectiblegroup)
    

while True :
    screen.fill("white")
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
    text1 = font.render("score1 = {}".format(score1),True,"#000000")
    screen.blit(text1,(50,50))

    text2 = font.render("score2 = {}".format(score2),True,"#000000")
    screen.blit(text2,(350,50))

    key = pygame.key.get_pressed()
    playergroup.update(key)
    collectiblegroup.update(key)

    playergroup.draw(screen)
    collectiblegroup.draw(screen)

    
    pygame.display.update()




