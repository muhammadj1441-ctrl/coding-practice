import pygame
pygame.init()

screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

green = (0,128,0)
blue = (0,0,255)

x = 300
y = 400

Lx = 0
Ly = 100

class Frog():
    def __init__(self):
        self.img = pygame.image.load('Frog.png').convert_alpha()
        self.img = pygame.transform.scale(self.img,(200,200))
        self.rect = self.img.get_rect()

    def draw(self,screen,Lx,Ly):
        screen.blit(self.img, (Lx,Ly))

Character = Frog()





class Log():
    def __init__(self):
        self.img = pygame.image.load('Log.png').convert_alpha()
        self.img = pygame.transform.scale(self.img,(200,200))
        self.rect = self.img.get_rect()
    def draw(self,screen,X,Y):
        screen.blit(self.img,(X,Y))
log = Log()


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                y -=20
            elif event.key == pygame.K_a:
                x-=20
            elif event.key == pygame.K_s:
                y+=20
            elif event.key == pygame.K_d:
                x+=20
    screen.fill((0,0,0))
    pygame.draw.rect(screen,green,(0,480,800,120))
    pygame.draw.rect(screen,blue,(0,360,800,120))
    pygame.draw.rect(screen,green,(0,240,800,120))
    pygame.draw.rect(screen,blue,(0,120,800,120))
    pygame.draw.rect(screen,green,(0,60,800,60))
    log.draw(screen,Lx,Ly)
    Character.draw(screen,x,y)

    pygame.display.flip()
    clock.tick(60)

