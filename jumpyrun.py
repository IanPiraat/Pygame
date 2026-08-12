import pygame
import random
pygame.init()
WIDTH =500
HEIGHT =500
playerstatus = 1
screen = pygame.display.set_mode((WIDTH,HEIGHT))
background = pygame.image.load("images/imagesjumpyrun/desertbackground.png")

playeridle = pygame.image.load("images/imagesjumpyrun/playeridle.png")
playerjump = pygame.image.load("images/imagesjumpyrun/playerjump.png")


briefcaseimage = pygame.image.load("images/imagesjumpyrun/briefcase.png")

clock = pygame.time.Clock()

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
        charge_seconds = charge / 1000
        jump_height = max(5, min(int(charge_seconds * 60), 120))
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
    def __init__(self, x, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.start_x = x
        self.reset()

    def reset(self):
        self.rect.x = self.start_x
        self.rect.y = random.randint(100, 400)
        self.active = True

    def update(self, player_rect):
        if not self.active:
            return
        if self.rect.centerx < player_rect.centerx:
            self.rect.x += 3
        else:
            self.rect.x -= 3
        if self.rect.right < 0 or self.rect.left > WIDTH:
            self.reset()

    def check_collision(self, player_rect):
        if self.active and self.rect.colliderect(player_rect):
            self.reset()
            return True
        return False









player = Player(100, 400, playeridle)
briefcase = Briefcase(WIDTH, briefcaseimage)
start = 0

while True :
    dt = clock.tick(60)
    screen.fill("white")
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

    player.update()
    briefcase.update(player.rect)
    if briefcase.check_collision(player.rect):
        

        screen.blit(background,(0,0))
        if briefcase.active:
            screen.blit(briefcase.image, briefcase.rect)
        if playerstatus == 1 :
            screen.blit(playeridle, player.rect)
        elif playerstatus == 0 :
            screen.blit(playerjump, player.rect)

    pygame.display.update()






