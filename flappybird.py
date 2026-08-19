import pygame
import random
pygame.init()
WIDTH =800
HEIGHT =700
screen = pygame.display.set_mode((WIDTH,HEIGHT))
background = pygame.image.load("images/imagesflappybird/Background.png")
flying = False
ground = pygame.image.load("images/imagesflappybird/ground.png")
ground = pygame.transform.scale(ground,(1600,250))
groundx = 0

flappymiddle = pygame.image.load("images/imagesflappybird/bird2.png")
flappyup = pygame.image.load("images/imagesflappybird/bird3.png")
flappydown = pygame.image.load("images/imagesflappybird/bird1.png")


images = [flappyup,flappymiddle,flappydown]
game = True
class bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__() 
        self.y = y
        self.x = x
        self.index = 0
        self.counter = 0
        self.velocity = 0
        self.image = images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = self.x,self.y
    def update(self) :
         if flying == True :
            self.velocity += 0.001
            if self.rect.bottom <= 625 :
                self.rect.y += self.velocity
            else :
                global game
                game = False
                self.image = images[1]
         if game == True :
             if pygame.mouse.get_pressed()[0] == 1 :
                 self.velocity = -0.55

             self.counter += 1
             if self.counter > 50 :
                 self.counter = 0
                 self.index += 1
                 if self.index >= 2 :
                     self.index = 0
                 self.image = images[self.index]
                        

            
        

flappy = bird(100,400)

flappygroup = pygame.sprite.Group()
flappygroup.add(flappy)

class pipes(pygame.sprite.Sprite):
    def __init__(self,x,y,angle):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load("images/imagesflappybird/pipe.png")
        self.angle = angle
        self.rect = self.image.get_rect()
        self.rect.center = self.x,self.y
        if self.angle == 1 :
            self.image = pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft = self.x,self.y - 100
        if self.angle == 0 :
            self.rect.topleft = self.x,self.y + 100
    def update(self) :
        if self.rect.right > 0 :
            self.rect.x -= 1
        else :
            self.kill()


pipegroup = pygame.sprite.Group()

pipefrequency = 1500
last_pipe = pygame.time.get_ticks() - pipefrequency








while True :
    screen.fill("white")
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN and game == True and flying == False :
            flying = True



    screen.blit(background,(0,0))
    screen.blit(ground,(groundx,600))
    if flying == True and game == True :
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > pipefrequency:
            height = random.randint(-100,100)
            bottompipe = pipes(800,700/2+height,0)
            toppipe = pipes(800,700/2+height,1)
            pipegroup.add(bottompipe)
            pipegroup.add(toppipe)

            last_pipe = time_now            
        pipegroup.update()    
    if game == True :
        groundx -= .5
        if groundx < -450 :
            groundx = 0

    flappygroup.update()        
    flappygroup.draw(screen)
    pipegroup.draw(screen)        
    pygame.display.update()





