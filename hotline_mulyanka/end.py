import pygame,os,sys, random
pygame.font.init()
pygame.init()
screenmaxx = 0
screenmaxy = 0
player_size = 1
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screenmaxx, screenmaxy))
pygame.display.set_caption("Мулянские Будни")
running = True
ui = [
    pygame.image.load('./data/textures/ui/blackscreen.png')    
]
myfont = pygame.font.Font('./font/rus8bit.otf', 128)
asd = pygame.font.Font('./font/rus8bit.otf', 15)
text1 = myfont.render('СКОРО', False, (255,0,255))
text2 = asd.render(' нажмите ESCAPE чтобы выйти',False,(255,0,255))
uilol = pygame.transform.scale(ui[0], (500,500))
def vivod():
    screen.blit(text2, (1000,800))
    screen.blit(text1, (500,500))
    screen.blit(uilol, (0,0))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    mouse_pos = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
    vivod()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()