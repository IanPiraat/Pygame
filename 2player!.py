
import random
import pygame
pygame.init()
WIDTH = 500
HEIGHT = 500
score1 = 0
score2 = 0
screen = pygame.display.set_mode((WIDTH, HEIGHT))
player_image = pygame.image.load("images/images 2player!/pirate/pirate.png")
player_image = pygame.transform.scale(player_image, (75, 75))

player_image2 = pygame.image.load("images/images 2player!/pirate/parrot.png")
player_image2 = pygame.transform.scale(player_image2, (75, 75))

collectible_image = pygame.image.load(r"images/images 2player!/pirate/damage.png")
collectible_image = pygame.transform.scale(collectible_image, (75, 75))

playergroup = pygame.sprite.Group()
collectiblegroup = pygame.sprite.Group()

font = pygame.font.SysFont("Arial", 24)


class payer1(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.x = x
        self.y = y
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y

    def update(self, k):
        if k[pygame.K_UP]:
            self.rect.y -= .51
        if k[pygame.K_DOWN]:
            self.rect.y += .51
        if k[pygame.K_RIGHT]:
            self.rect.x += .51
        if k[pygame.K_LEFT]:
            self.rect.x -= .51


class payer2(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.x = x
        self.y = y
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y

    def update(self, k):
        if k[pygame.K_w]:
            self.rect.y -= .51
        if k[pygame.K_s]:
            self.rect.y += .51
        if k[pygame.K_d]:
            self.rect.x += .51
        if k[pygame.K_a]:
            self.rect.x -= .51


class collectible(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.x = x
        self.y = y
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def respawn(self):
        margin_x = self.rect.width // 2
        margin_y = self.rect.height // 2
        new_x = random.randint(margin_x, WIDTH - margin_x)
        new_y = random.randint(margin_y, HEIGHT - margin_y)
        self.rect.center = (new_x, new_y)


player1 = payer1(175, 250, player_image)
player2 = payer2(175, 300, player_image2)
playergroup.add(player1, player2)

collectible_item = collectible(250, 100, collectible_image)
collectiblegroup.add(collectible_item)
collectible_item.respawn()

while True:
    screen.fill("white")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    text1 = font.render("score1 = {}".format(score1), True, "#000000")
    screen.blit(text1, (50, 50))
    text2 = font.render("score2 = {}".format(score2), True, "#000000")
    screen.blit(text2, (350, 50))

    key = pygame.key.get_pressed()
    playergroup.update(key)
    collectiblegroup.update(key)

    if pygame.sprite.spritecollideany(player1, collectiblegroup):
        score1 += 1
        collectible_item.respawn()
        while collectible_item.rect.colliderect(player1.rect) or collectible_item.rect.colliderect(player2.rect):
            collectible_item.respawn()

    if pygame.sprite.spritecollideany(player2, collectiblegroup):
        score2 += 1
        collectible_item.respawn()
        while collectible_item.rect.colliderect(player1.rect) or collectible_item.rect.colliderect(player2.rect):
            collectible_item.respawn()

    playergroup.draw(screen)
    collectiblegroup.draw(screen)

    pygame.display.update()




