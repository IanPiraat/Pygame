import pygame
pygame.init()
WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
drawtrue = False
first = True
shape = "rect"

class Rect():
    def __init__(self, x, y, w, l, color):
        self.x = x
        self.y = y
        self.w = w
        self.l = l
        self.color = color

    def drawr(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.l))

class Circle():
    def __init__(self, x, y, r, color):
        self.x = x
        self.y = y
        self.r = r
        self.color = color

    def drawc(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

class Line():
    def __init__(self, x1, y1, x2, y2, color):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color

    def drawl(self):
        pygame.draw.line(screen, self.color, (self.x1, self.y1), (self.x2, self.y2), 3)

r1 = None
c1 = None
l1 = None

while True:
    screen.fill("white")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
            drawtrue = True
            shape = "rect"
            first = True
    if keys[pygame.K_c]:
            drawtrue = True
            shape = "circle"
            first = True
    if keys[pygame.K_l]:
            drawtrue = True
            shape = "line"
            first = True

    if drawtrue == True:
            if first == True:
                pos = pygame.mouse.get_pos()
                first = False
                if shape == "rect":
                    r1 = Rect(pos[0], pos[1], 50, 20, "red")
                elif shape == "circle":
                    c1 = Circle(pos[0], pos[1], 25, "red")
                else:
                    l1 = Line(pos[0], pos[1], pos[0] + 50, pos[1], "red")

    if r1:
            r1.drawr()
    if c1:
            c1.drawc()
    if l1:
            l1.drawl()

    pygame.display.update()




