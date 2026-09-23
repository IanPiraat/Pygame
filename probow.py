import pygame
import math
pygame.init()
WIDTH = 960
HEIGHT =549
playercharge = False
screen = pygame.display.set_mode((WIDTH,HEIGHT))

background = pygame.image.load("images/images probow/bg.png")
playeridleL = pygame.image.load("images/images probow/playeridle.png")
playeridleR = pygame.image.load("images/images probow/playeridle.png")
playeridleR = pygame.transform.flip(playeridleR,True,False)
playerchargeL = pygame.image.load("images/images probow/playercharge.png")
playerchargeR = pygame.image.load("images/images probow/playercharge.png")
playerchargeL = pygame.transform.flip(playerchargeR,True,False)
background  = pygame.transform.scale(background,(960,549))
arrow = pygame.image.load("images/images probow/arrow.png")
arrowR = pygame.image.load("images/images probow/arrow.png")
arrowR = pygame.transform.flip(arrowR,True,False)
arrowR = pygame.transform.scale(arrowR,(50,50))
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
    def __init__(self,x,y,image,velocity,charge,damage,direction) :
        super().__init__()
        self.angle = 0
        self.x = x 
        self.y = y
        self.image = image 
        self.original_image =image
        self.velocity = velocity
        self.charge = charge
        self.damage = damage
        self.direction = direction
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        mousex, mouse_y = pygame.mouse.get_pos()
        dx = mousex - self.x
        dy = mouse_y - self.y
        self.angle = math.degrees(math.atan2(-dy,dx))
        self.image = pygame.transform.rotate(self.original_image,self.angle)
        self.rect = self.image.get_rect()
                
    def update(self) :
        
        if self.direction == "left" :
            if self.rect.x < 960 and (self.rect.y > 0 or self.rect.y < HEIGHT) :
                self.x += math.cos(math.radians(self.angle)) * self.velocity
                self.y -= math.sin(math.radians(self.angle)) * self.velocity 
                self.rect.center = (self.x, self.y)
        
            else :
                self.kill()
        elif self.direction == "right" :
             if self.rect.x > 0 and (self.rect.y > 0 or self.rect.y < HEIGHT+100) :
                    self.x -= math.cos(math.radians(self.angle)) * self.velocity
                    self.y -= math.sin(math.radians(self.angle)) * self.velocity 
                    self.rect.center = (self.x, self.y)
             else :
                self.kill()       
        
        
player1 = player(100,400,health=100,image=playeridleL,status="idle",)
enemy = player(860,400,100,playeridleR,"enemy")
  
playergroup = pygame.sprite.Group()
enemygroup = pygame.sprite.Group()
Arrowgroup = pygame.sprite.Group()
EnemyArrowGroup = pygame.sprite.Group()
playergroup.add(player1)
enemygroup.add(enemy)


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
            Arrow = arrows(player1.rect.right,player1.rect.centery,image=arrow,velocity=5,charge=100,damage=10,direction="left")
            Arrowgroup.add(Arrow)
            Arrow2 = arrows(WIDTH/2,HEIGHT/2,image=arrow,velocity=5,charge=100,damage=10,direction="right")
            EnemyArrowGroup.add(Arrow2)
            print(Arrow2.rect.right,Arrow2.rect.centery)

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_w :
                    pos = pygame.mouse.get_pos()
                    shootarrow.play()
                    #Arrow = arrows(enemy.rect.right,enemy.rect.centery,image=arrowR,velocity=5,charge=100,damage=10,direction="right")
                    Arrow2 = arrows(WIDTH/2,HEIGHT/2,image=arrow,velocity=-5,charge=100,damage=10,direction="right")
                    EnemyArrowGroup.add(Arrow2)
                    print(Arrow2.rect.right,Arrow2.rect.centery)
                    
             
    Arrowgroup.update()
    EnemyArrowGroup.update()
    Arrowgroup.draw(screen)
    EnemyArrowGroup.draw(screen)
    playergroup.draw(screen)
    enemygroup.draw(screen)
    

    pygame.display.update()




