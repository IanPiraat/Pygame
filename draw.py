import pygame
pygame.init()
WIDTH =500
HEIGHT =500
screen = pygame.display.set_mode((WIDTH,HEIGHT))
class drawr() :
    def __init__(self,x,y,h,w,color) :
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.color = color
    def draw(self) :
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.w,self.h))
class drawc():
    def __init__ (self,x,y,color,r):
        self.x = x
        self.y = y
        self.color = color
        self.r = r
    def draw(self) :
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.r)

r1 = drawr(20,30,50,150,"blue")
r2 = drawr(40,50,60,205,"green")
c1 = drawc (30,30,"red",50)











while True :
    screen.fill("white")
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()

    r1.draw()
    r2.draw()
    c1.draw()
    pygame.display.update()
