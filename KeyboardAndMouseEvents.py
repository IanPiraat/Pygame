import pygame
pygame.init()
WIDTH =500
HEIGHT =500
color1 = 1
screen = pygame.display.set_mode((WIDTH,HEIGHT))
rectangle = []
class Rect() :
    def __init__(self,x,y,w,l,color):
        self.x = x
        self.y = y
        self.w = w
        self.l = l
        self.color = color
    def drawr(self) :
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.w,self.l))
    def up(self) :
        self.y -= .1
    def down(self) :
        self.y += .1
    def right(self) :
        self.x += .1
    def left(self) :
        self.x -= .1   
                 
        

r1 = Rect(250,250,50,20,"red")
r2 = Rect(250,250,50,20,"blue")
r3 = None
while True :
    screen.fill("white")
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
        # if event.type == pygame.KEYDOWN :
        #     if event.key == pygame.K_w :
        #         r1.up()
        #     elif event.key == pygame.K_s :
        #         r1.down()
        #     elif event.key == pygame.K_d :
        #         r1.right()
        #     elif event.key == pygame.K_a :
        #         r1.left()    
        if event.type == pygame.MOUSEBUTTONDOWN :
            pos = pygame.mouse.get_pos()
            screen.fill("white")
            r3 = Rect(pos[0],pos[1],50,20,"green")
            
            print("Greenrectangle")
        if event.type == pygame.MOUSEBUTTONUP :
            r1.l += 50
        if event.type == pygame.MOUSEMOTION :
            pos = pygame.mouse.get_pos()
            r2.x = pos[0] 
            r2.y = pos[1]   
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] :
        r1.up()
    if keys[pygame.K_s] :
        r1.down()
    if keys[pygame.K_d] :
        r1.right()
    if keys[pygame.K_a] :
        r1.left()        
                                
    r1.drawr()
    r2.drawr()
    if r3:
        r3.drawr()
    

    pygame.display.update()




