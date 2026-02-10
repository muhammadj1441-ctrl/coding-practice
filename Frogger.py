import pygame
pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

green = (0,128,0)
blue = (0,0,255)
grey = (128,128,128)



goal_rect = pygame.Rect(0, 60, WIDTH, 60)
font = pygame.font.Font(None, 36)

score = 0
lives = 3
level = 0


#FROG
class Frog():
    def __init__(self):
        self.img = pygame.image.load('Frog.png').convert_alpha()
        self.img = pygame.transform.scale(self.img,(60,60))
        self.rect = self.img.get_rect()
        self.rect = self.rect.inflate(-20, -20)
        self.rect.topleft = (350, 500)


    def draw(self,screen):
        screen.blit(self.img, self.rect)

Character = Frog()

#LOGS
class Log():
    def __init__(self,x,y):
        self.img = pygame.image.load('Log.png').convert_alpha()
        self.img = pygame.transform.scale(self.img,(100,100))
        self.rect = self.img.get_rect()
        self.rect = self.rect.inflate(-20, -20)
        self.rect.y = y
        self.rect.x = x
        self.speed = 2

    def draw(self,screen):
        screen.blit(self.img,self.rect)

    def update(self):
        self.rect.x += self.speed
        if self.rect.left > WIDTH:
            self.rect.left = -self.rect.width

logs = [Log(0,100),
       Log(0,150),
        Log(200,100),
        Log(200,150),
        Log(400,100),
        Log(400,150),
        Log(600,100),
        Log(600,150),

        ]


#CARS
class Car():
    def __init__(self,x,y):
        self.img = pygame.image.load('Car.png').convert_alpha()
        self.img = pygame.transform.scale(self.img,(80,80))
        self.rect = self.img.get_rect()
        self.rect = self.rect.inflate(-20, -20)
        self.rect.y = y
        self.rect.x = x
        self.speed = 2

    def update(self):
        self.rect.x += self.speed
        if self.rect.left > WIDTH:
            self.rect.right = 0


    def draw(self,screen):
        screen.blit(self.img, self.rect)
cars = [Car(-80,360),
        Car(-300,360),
        Car(-600,360)]


#GAME LOOP
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                Character.rect.y -= 40
            elif event.key == pygame.K_s:
                Character.rect.y += 20
            elif event.key == pygame.K_a:
                Character.rect.x -= 20
            elif event.key == pygame.K_d:
                Character.rect.x += 20

	
    screen.fill((0,0,0))
    pygame.draw.rect(screen,green,(0,480,800,120))
    pygame.draw.rect(screen,grey,(0,360,800,120))
    pygame.draw.rect(screen,green,(0,240,800,120))
    pygame.draw.rect(screen,blue,(0,120,800,120))
    pygame.draw.rect(screen,green,(0,60,800,60))
    water_rect = pygame.Rect(0, 120, 800, 120)

	#REACH END OF LEVEL DETECTION + ADJUST PER LEVEL
    if Character.rect.colliderect(goal_rect):
        score += 10
        Character.rect.topleft = (350, 500)
        level += 1
        for car in cars:
            car.speed += 0.5
        for log in logs:
            log.speed += 0.3







    score_text = font.render(f"Score: {score}", True, (255, 0, 0))
    screen.blit(score_text, (10, 10))


    lives_text = font.render(f"Lives: {lives}", True, (255, 255, 255))
    screen.blit(lives_text, (10, 50))


    level_text = font.render(f"Level: {level}", True, (255, 255, 255))
    screen.blit(level_text, (10, 90))

	#DRAW CHARACTER, LOGS, CARS

	Character.draw(screen)

	for log in logs:
        log.update()
        log.draw(screen)

	
    for car in cars:
        car.update()
        car.draw(screen)


	#COLLISONS

    for car in cars:
        if Character.rect.colliderect(car.rect):
            lives -= 1
            Character.rect.topleft = (350, 500)
            if lives <= 0:
                print("GAME OVER")
                run = False

    #stick to log
    on_log = False
    for log in logs:
        if Character.rect.colliderect(log.rect):
            on_log = True
            Character.rect.x += log.speed

    if Character.rect.colliderect(water_rect) and not on_log:
        lives -= 1
        Character.rect.topleft = (350, 500)
        if lives <= 0:
            print("GAME OVER")
            run = False

    pygame.display.flip()
    clock.tick(60)


