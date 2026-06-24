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
            
player1 = player(400,500,"red")
player2 = player(1200,500,"yellow")

while True :
    screen.fill("white")
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
    screen.blit(p_space,(0,0))

    screen.blit(player1.image,player1.rect.center)

    screen.blit(player2.image,player2.rect.center)
    pygame.draw.rect(screen,"black",pygame.Rect(800,0,25,1000))
    keys_pressed = pygame.key.get_pressed()
    player1.move_ship(keys_pressed)
    player2.move_ship(keys_pressed)


    pygame.display.update()




