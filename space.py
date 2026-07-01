import pygame
pygame.init()
WIDTH =1600
HEIGHT =1000
screen = pygame.display.set_mode((WIDTH,HEIGHT))
p_space = pygame.image.load("images\imagespace\Image20260617164523.png")
p_space = pygame.transform.scale(p_space,(1600,1000))

p_player1 = pygame.image.load("images\imagespace\Image20260617164516.png")
p_player1 = pygame.transform.scale(p_player1,(250,200))
p_player1 = pygame.transform.rotate(p_player1,270)

p_player2 = pygame.image.load("images\imagespace\Image20260617164520.png")
p_player2 = pygame.transform.scale(p_player2,(250,200))
p_player2 = pygame.transform.rotate(p_player2,90)

bullets1 = pygame.sprite.Group()
bullets2 = pygame.sprite.Group()





font1 = pygame.font.SysFont("Sans Serif",50)
class player(pygame.sprite.Sprite) :
    def __init__(self,x,y,color):
        super().__init__()
        self.x = x
        self.y = y 
        self.color = color
        if self.color == "red" :
            self.image = p_player1
        elif self.color == "yellow" :
            self.image = p_player2
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)
        self.health = 100
    def move_ship(self,k)  :
        if self.color == "red" :
            if k[pygame.K_w] and self.rect.y > -200 :
                self.rect.y -= 5 
            if k[pygame.K_s]  and self.rect.y < 750 : 
                self.rect.y += 5
            if k[pygame.K_d] and self.rect.x < 525 :
                self.rect.x += 5    
            if k[pygame.K_a] and self.rect.x > -200 :
                self.rect.x -= 5
        elif self.color == "yellow" :
            if k[pygame.K_UP] and self.rect.y > -200:
                self.rect.y -= 5
            if k[pygame.K_DOWN] and self.rect.y < 750  :
                self.rect.y += 5
            if k[pygame.K_RIGHT] and self.rect.x < 1450 :
                self.rect.x += 5    
            if k[pygame.K_LEFT] and self.rect.x > 700 :
                self.rect.x -= 5
class bullet(pygame.sprite.Sprite) :
    def __init__(self,x,y,color):
        super().__init__()
        self.x = x
        self.y = y 
        self.color = color
        self.rect = pygame.Rect(self.x,self.y,5,5)
    def update(self) :
        if self.color == "red" :
            self.rect.x += 5
            if self.rect.x > 1600 :
                self.kill()

        elif self.color == "yellow" :
            self.rect.x -= 5
            if self.rect.x < 0 :
                self.kill()




    


player1 = player(400,500,"red")
player2 = player(1200,500,"yellow")



while True :
    screen.fill("white")
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()

    keys = pygame.key.get_pressed() 

    if keys[pygame.K_SPACE] :
        red = bullet(player1.rect.x,player1.rect.y,"red")
        bullets1.add(red)

    if keys[pygame.K_RSHIFT] :
        yellow = bullet(player2.rect.x,player2.rect.y,"yellow")
        bullets2.add(yellow)




            
    screen.blit(p_space,(0,0))

    screen.blit(player1.image,player1.rect.center)
    text1 = font1.render("Health = {}".format(player1.health),True,"#c2380e")
    text2 = font1.render("Health = {}".format(player2.health),True,"#ffe100")
    screen.blit(text1,(50,950))
    screen.blit(text2,(1350,950))

   
    screen.blit(player2.image,player2.rect.center)
    pygame.draw.rect(screen,"black",pygame.Rect(800,0,25,1000))
    keys_pressed = pygame.key.get_pressed()
    player1.move_ship(keys_pressed)
    player2.move_ship(keys_pressed)

    for redbullet in bullets1 :
        pygame.draw.rect(screen,"red",redbullet.rect)

    for yellowbullet in bullets2 :
        pygame.draw.rect(screen,"yellow",yellowbullet.rect)

    bullets1.update()
    bullets2.update()

    pygame.display.update()




