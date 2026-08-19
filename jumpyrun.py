import pygame
import random
pygame.init()
WIDTH =500
HEIGHT =500
score = 0
playerstatus = 1
screen = pygame.display.set_mode((WIDTH,HEIGHT))
background = pygame.image.load("images/imagesjumpyrun/desertbackground.png")
score_background = pygame.image.load("images/imagesjumpyrun/space.png")

    #background = pygame.image.load("images\imagesjumpyrun\space.png")    

playeridle = pygame.image.load("images/imagesjumpyrun/playeridle.png")
playerjump = pygame.image.load("images/imagesjumpyrun/playerjump.png")

font1 = pygame.font.SysFont("Sans Serif",50)

briefcaseimages = [
    "images/imagesjumpyrun/parrot.png",
    "images/imagesjumpyrun/briefcase.png"
]


clock = pygame.time.Clock()


music = pygame.mixer.Sound("sounds\spacesound\sounds jumpyrun\Lexica - Helios.wav")




class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.x = x
        self.y = y
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.ground_y = self.rect.y
        self.jumping = False
        self.jump_target = self.rect.y

    def start_jump(self, charge):
        charge_seconds = charge / 400
        jump_height = max(1, min(int(charge_seconds * 500), 240))
        if self.rect.y == self.ground_y:
            self.jump_target = self.ground_y - jump_height
            self.jumping = True

    def update(self):
        if self.jumping:
            if self.rect.y > self.jump_target:
                self.rect.y -= 3
            else:
                self.jumping = False
        elif self.rect.y < self.ground_y:
            self.rect.y += 3
class Briefcase(pygame.sprite.Sprite):
    def __init__(self, x, image, is_parrot):
        super().__init__()
        self.image = image
        self.is_parrot = is_parrot
        self.x = x
        self.y = random.randint(300,500)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x,self.y
        self.start_x = x
        self.active = True

    def update(self):
        global score
        print(self.rect.x,player.rect.x)
        if self.rect.x > 50 :
            self.rect.x -= 3
        else:
            self.kill()
            score -= 1
            
    def check_collision(self, player_rect):
        global score
        if self.active and self.rect.colliderect(player_rect):
            self.kill()
            if self.is_parrot:
                score += 2
            else :
                score += 1    
            return True
        return False









player = Player(100, 450, playeridle)
playergroup = pygame.sprite.Group()
briefcasegroup = pygame.sprite.Group()

playergroup.add(player)
briefcase = None
start = 0
count = 0
music.play(-1)
while True :
    dt = clock.tick(60)
    count += 1
    
    if score >= 5:
        background = score_background
    screen.blit(background,(0,0))
    
    if count > 0 and count % 300 == 0 :
        briefcasepath = random.choice(briefcaseimages)
        briefcaseimage = pygame.image.load(briefcasepath)
        briefcase = Briefcase(WIDTH, briefcaseimage, briefcasepath.endswith("parrot.png"))
        briefcasegroup.add(briefcase)
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                start = pygame.time.get_ticks()
                playerstatus = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                stop = pygame.time.get_ticks()
                playerstatus = 1
                chargetime = stop - start
                player.start_jump(chargetime)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                playerstatus = 0


    text1 = font1.render("score = {}".format(score),True,"#c2380e")        

    playergroup.update()
    screen.blit(text1,(0,0))
    briefcasegroup.update()
    for briefcase in briefcasegroup :
        if briefcase.check_collision(player.rect):
            

            screen.blit(background,(0,0))
            if briefcase.active:
                screen.blit(briefcase.image, briefcase.rect)
            if playerstatus == 1 :
                screen.blit(playeridle, player.rect)
            elif playerstatus == 0 :
                screen.blit(playerjump, player.rect)
    playergroup.draw(screen)
    briefcasegroup.draw(screen)
    pygame.display.update()






