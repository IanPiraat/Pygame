import pygame
import random
import time
pygame.init()
soundplayed = False
WIDTH =800
HEIGHT =700
replaydeath = 0
score = 0
screen = pygame.display.set_mode((WIDTH,HEIGHT))
background = pygame.image.load("images/imagesflappybird/Background.png")
flying = False
ground = pygame.image.load("images/imagesflappybird/ground.png")
ground = pygame.transform.scale(ground,(1600,250))
groundx = 0

flappymiddle = pygame.image.load("images/imagesflappybird/bird2.png")
flappyup = pygame.image.load("images/imagesflappybird/bird3.png")
flappydown = pygame.image.load("images/imagesflappybird/bird1.png")

music = pygame.mixer.Sound("sounds/spacesound/sounds flappybird/bgmusic.wav")
death = pygame.mixer.Sound("sounds/spacesound/sounds flappybird/death.wav")

font = pygame.font.SysFont("Arial", 24)
font2 = pygame.font.SysFont("Arial",55)
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
         global replaydeath
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







music.play(-1)
while True :
    
    screen.fill("white")
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN and game == True and flying == False :
            flying = True
        if event.type == pygame.KEYDOWN and game == False and event.key == pygame.K_RETURN :
            soundplayed = False
            pipegroup.empty()
            flappy.rect.x = 100
            flappy.rect.y = 200
            game = True
        if game == False and soundplayed == False :
            death.play()
            soundplayed = True
            
            
            
            

            
            


    
    screen.blit(background,(0,0))
    screen.blit(ground,(groundx,600))
    text1 = font.render("score = {}".format(score), True, "#000000")
    screen.blit(text1, (50, 50))
    if pygame.sprite.groupcollide(flappygroup,pipegroup,False,False) :
        game = False
    if game == False :
        text2 = font2.render("game over, press enter to reset", True, "#000000")
        screen.blit(text2, (5,350))
        score = 0
        


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
        for pipe in pipegroup:    
            if pipe.rect.left < flappy.rect.left :
                score += 1 
                pipe.kill()
    flappygroup.update()        
    flappygroup.draw(screen)
    pipegroup.draw(screen)        
    pygame.display.update()





