import pygame, sys, random
pygame.font.init()
pygame.init()
running = True
x = 0
y = 0
vectorx = 0
vectory = 0
screenmaxx = 0
screenmaxy = 0
start_pic = pygame.image.load('./data/textures/mainmenu/play.png')
start_pic = pygame.image.load('./data/textures/mainmenu/play.png')
start_pic = pygame.image.load('./data/textures/mainmenu/play.png')
start_pic = pygame.image.load('./data/textures/mainmenu/play.png') 
myfont = pygame.font.Font('./font/rus8bit.otf', 30)
screen = pygame.display.set_mode((screenmaxx, screenmaxy))
while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
pygame.quit()
sys.exit()