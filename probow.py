import pygame
import math
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
shootarrow = pygame.mixer.Sound("sounds/spacesound/probow sounds/tonenger-kiraful-go-arrow-release-sound-319709.wav")
music = pygame.mixer.Sound("sounds/spacesound/probow sounds/prettyjohn1-soft-499242.wav")
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
        self.angle = 0
        self.x = x 
        self.y = y
        self.image = image 
        self.original_image =image
        self.velocity = velocity
        self.charge = charge
        self.damage = damage
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        mousex, mouse_y = pygame.mouse.get_pos()
        dx = mousex - self.x
        dy = mouse_y - self.y
        self.angle = math.degrees(math.atan2(-dy,dx))
        self.image = pygame.transform.rotate(self.original_image,self.angle)
        self.rect = self.image.get_rect()
                
    def update(self) :
        
        
        if self.rect.x < 960 and (self.rect.y > 0 or self.rect.y < HEIGHT) :
            self.x += math.cos(math.radians(self.angle)) * self.velocity
            self.y -= math.sin(math.radians(self.angle)) * self.velocity 
            self.rect.center = (self.x, self.y)
        
        else :
            self.kill()
        
        
player1 = player(100,400,health=100,image=playeridle,status="idle",)
    
playergroup = pygame.sprite.Group()
Arrowgroup = pygame.sprite.Group()
playergroup.add(player1)


music.play(-1)





while True :
    screen.fill("white")
    screen.blit(background,(0,0))
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.MOUSEBUTTONDOWN :
            pos = pygame.mouse.get_pos()
            shootarrow.play()
            Arrow = arrows(player1.rect.right,player1.rect.centery,image=arrow,velocity=5,charge=100,damage=10,)
            Arrowgroup.add(Arrow)
             
    Arrowgroup.update()
        
    Arrowgroup.draw(screen)
    playergroup.draw(screen)

    pygame.display.update()




