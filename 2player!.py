import pygame
pygame.init()
WIDTH =500
HEIGHT =500
screen = pygame.display.set_mode((WIDTH,HEIGHT))
player_image = pygame.image.load("images/images 2player!/pirate/pirate.png")
player_image = pygame.transform.scale(player_image,(75,75))

player_image2 = pygame.image.load("images/images 2player!/pirate/parrot.png")
player_image2 = pygame.transform.scale(player_image2,(75,75))

class payer1() :
    def __init__(self,x,y,image):
        self.x = x
        self.y = y
        self.image = image
    def drawr(self) :
        screen.blit(self.image,(self.x,self.y))
    def up(self) :
        self.y -= .1
    def down(self) :
        self.y += .1
    def right(self) :
        self.x += .1
    def left(self) :
        self.x -= .1
class payer2() :
    def __init__(self,x,y,image):
        self.x = x
        self.y = y
        self.image = image
    def drawr1(self) :
        screen.blit(self.image,(self.x,self.y))
    def up1(self) :
        self.y -= .1
    def down1(self) :
        self.y += .1
    def right1(self) :
        self.x += .1
    def left1(self) :
        self.x -= .1           





player1 = payer1(175,250,player_image)
player2 = payer2(175,300,player_image2)

while True :
    screen.fill("white")
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] :
        player1.up()
    if keys[pygame.K_s] :
        player1.down()
    if keys[pygame.K_d] :
        player1.right()
    if keys[pygame.K_a] :
        player1.left()


    if keys[pygame.K_UP] :
        player2.up1()
    if keys[pygame.K_DOWN] :
        player2.down1()
    if keys[pygame.K_RIGHT] :
        player2.right1()
    if keys[pygame.K_LEFT] :
        player2.left1()            





    player1.drawr()
    player2.drawr1()
    pygame.display.update()




