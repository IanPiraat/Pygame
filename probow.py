import pygame
import math
pygame.init()
WIDTH = 960
HEIGHT =549
playercharge = False
screen = pygame.display.set_mode((WIDTH,HEIGHT))
font1 = pygame.font.SysFont("Sans Serif",50)

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
        health1 = health
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        
class arrows(pygame.sprite.Sprite) :
    def __init__(self,x,y,image,velocity,charge,damage,direction,target) :
        super().__init__()
       # self.angle = 0
        self.x = x 
        self.y = y
        #self.original_image =image
        self.velocity = velocity
        self.charge = charge
        self.damage = damage
        tx,ty = target
        dx = tx - self.x
        dy = ty - self.y
        angle = math.atan2(dy,dx)
        self.vx = math.cos(angle) * self.velocity
        self.vy = math.sin(angle) * self.velocity
        self.direction = direction
        self.image = pygame.transform.rotate(image, -math.degrees(angle))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        
        
                
    def update(self) :
        
        # if self.direction == "left" :
            
        #         self.x += math.cos(math.radians(self.angle)) * self.velocity
        #         self.y -= math.sin(math.radians(self.angle)) * self.velocity 
        #         self.rect.center = (self.x, self.y)
        
           
        # elif self.direction == "right" :
             
        #             self.x -= math.cos(math.radians(self.angle)) * self.velocity
        #             self.y -= math.sin(math.radians(self.angle)) * self.velocity 
        #             self.rect.center = (self.x, self.y)
        self.x += self.vx
        self.y += self.vy
        self.rect.center = self.x,self.y
        if self.rect.right < 0 or self.rect.left > WIDTH or self.rect.top > HEIGHT or self.rect.bottom < 0 :  
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


clock = pygame.time.Clock()


while True :
    clock.tick(60)
    screen.fill("white")
    screen.blit(background,(0,0))
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.MOUSEBUTTONDOWN :
            pos = pygame.mouse.get_pos()
            shootarrow.play()
            Arrow = arrows(player1.rect.right,player1.rect.centery,image=arrow,velocity=5,charge=100,damage=10,direction="left",target=pygame.mouse.get_pos())
            Arrowgroup.add(Arrow)
            #Arrow2 = arrows(enemy.rect.right,enemy.rect.centery,image=arrowR,velocity=5,charge=100,damage=10,direction="right")
            #EnemyArrowGroup.add(Arrow2)    

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_w :
                    pos = pygame.mouse.get_pos()
                    shootarrow.play()
                    Arrow2 = arrows(enemy.rect.left,enemy.rect.centery,image=arrow,velocity=5,charge=100,damage=10,direction="right",target=player1.rect.center)
                    EnemyArrowGroup.add(Arrow2)
                    print(Arrow2.rect.right,Arrow2.rect.centery)

                    print("enemy arrows:",len(EnemyArrowGroup))
    text1 = font1.render("p1 health = {}".format(player1.health),True,"#c2380e")
    screen.blit(text1,(600,30))            
             
    Arrowgroup.update()
    EnemyArrowGroup.update()
    Arrowgroup.draw(screen)
    EnemyArrowGroup.draw(screen)
    playergroup.draw(screen)
    enemygroup.draw(screen)
    

    pygame.display.update()




