import pygame
pygame.init()
WIDTH =500
HEIGHT =500
screen = pygame.display.set_mode((WIDTH,HEIGHT))
# class drawr() :
#     def __init__(self,x,y,h,w,color) :
#         self.x = x
#         self.y = y
#         self.h = h
#         self.w = w
#         self.color = color
#     def draw(self) :
#         pygame.draw.rect(screen,self.color,(self.x,self.y,self.w,self.h))
class drawc():
    def __init__ (self,x,y,color,r):
        self.x = x
        self.y = y
        self.color = color
        self.r = r
        self.uy = 100
        self.ux = 195
    def draw(self) :
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.r)
    def update(self,dt) :
        initial = self.uy
        self.uy += 2000 * dt
        self.y += (initial + self.uy) * 0.5 * dt
        if self.y > HEIGHT - self.r:
            self.y = HEIGHT - self.r
            self.uy = -self.uy* 0.9
        self.x += self.ux * dt
        if self.x > WIDTH - self.r:
           self.x =WIDTH-self.r
           self.ux = - self.ux  


        
    
#r1 = drawr(20,30,50,150,"blue")
#r2 = drawr(40,50,60,205,"green")
c1 = drawc (20,30,"red",50)
c2 = drawc (19,30,"blue",25)
c3 = drawc (500,30,"green",10)
c4 = drawc (250,50,"purple",10)
c5 = drawc (550,30,"brown",10)



clock = pygame.time.Clock()









while True :
    dt = clock.tick(60) / 1000
    screen.fill("white")
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()

    #r1.draw()
    #r2.draw()
    c1.draw()
    c1.update(dt)
    c2.draw()
    c2.update(dt)
    c3.draw()
    c3.update(dt)
    c4.draw()
    c4.update(dt)
    c5.draw()
    c5.update(dt)
    


    pygame.display.update()
