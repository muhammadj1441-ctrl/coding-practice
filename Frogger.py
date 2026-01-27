import pygame
pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

green = (0,128,0)
blue = (0,0,255)
grey = (128,128,128)

x = 350
y = 500

Lx = 0
Ly = 100

Cx = 0
Cy = 0

class Frog():
    def __init__(self):
        self.img = pygame.image.load('Frog.png').convert_alpha()
        self.img = pygame.transform.scale(self.img,(80,80))
        self.rect = self.img.get_rect()

    def draw(self,screen,x,y):
        self.rect.topleft = (x,y)
        screen.blit(self.img, self.rect)

Character = Frog()


class Log():
    def __init__(self):
        self.img = pygame.image.load('Log.png').convert_alpha()
        self.img = pygame.transform.scale(self.img,(180,180))
        self.rect = self.img.get_rect()

    def draw(self,screen,X,Y):
        screen.blit(self.img,(X,Y))
log = Log()


class Car():
    def __init__(self):
        self.img = pygame.image.load('Car.png').convert_alpha()
        self.img = pygame.transform.scale(self.img,(80,80))
        self.rect = self.img.get_rect()
        self.rect.y = 360
        self.rect.x = -80
        self.speed = 2

    def update(self):
        self.rect.x += self.speed
        if self.rect.left > WIDTH:
            self.rect.right = 0


    def draw(self,screen):
        screen.blit(self.img, self.rect)
car = Car()



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
    pygame.draw.rect(screen,grey,(0,360,800,120))
    pygame.draw.rect(screen,green,(0,240,800,120))
    pygame.draw.rect(screen,blue,(0,120,800,120))
    pygame.draw.rect(screen,green,(0,60,800,60))
    log.draw(screen,Lx,Ly)
    car.update()
    Character.draw(screen, x, y)
    car.draw(screen)


    if Character.rect.colliderect(car.rect):
        print("GAME OVER")
        run = False

    pygame.display.flip()
    clock.tick(60)
