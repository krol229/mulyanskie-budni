import pygame, sys, random, math, subprocess
pygame.font.init()
pygame.init()
pygame.display.set_caption("Мулянские Будни")
running = True
x = 0
y = 0
vectorx = 0
vectory = 0
screenmaxx = 0
screenmaxy = 0
player_size = 1
screen = pygame.display.set_mode((screenmaxx, screenmaxy))
myfont = pygame.font.Font('./font/rus8bit.otf', 30)
kluch = 0
ui = [
    pygame.image.load('./data/textures/ui/blackscreen.png')    
]
lungin = [
    pygame.image.load('./data/textures/dialog/lungin.png')
]
location2 = [
    pygame.image.load('./data/textures/resources/2map.png'),
    pygame.image.load('./data/textures/resources/malungin.png'),
    pygame.image.load('./data/textures/resources/2tree.png'),
    pygame.image.load('./data/textures/resources/tree.png'),
    pygame.image.load('./data/textures/resources/3tree.png'),
]
misha = [
    #malgin
    pygame.image.load('./data/textures/mihuyek/malgin/malginumer.png'),
    pygame.image.load('./data/textures/mihuyek/malgin/maliginleftudar.png'),
    pygame.image.load('./data/textures/mihuyek/malgin/maliginrightudar.png'),
    #maligin
    pygame.image.load('./data/textures/mihuyek/maligin/maliginumer.png'),#умер 
    pygame.image.load('./data/textures/mihuyek/maligin/maliginumer2.png'),#умер 2
    pygame.image.load('./data/textures/mihuyek/maligin/mishaidle.png'),#стоит
    pygame.image.load('./data/textures/mihuyek/maligin/mishaleftudar.png'),#удар слева
    pygame.image.load('./data/textures/mihuyek/maligin/misharightudar.png'),#удар справа
    pygame.image.load('./data/textures/mihuyek/maligin/mishapravo.png'),#шаг правой ноги
    pygame.image.load('./data/textures/mihuyek/maligin/mishalevo.png'),#шаг левой ноги
]
mishahodit = [
    pygame.image.load('./data/textures/mihuyek/malgin/maliginidle.png'),
    pygame.image.load('./data/textures/mihuyek/malgin/maliginlevo.png'),
    pygame.image.load('./data/textures/mihuyek/malgin/maliginpravo.png'),
]
uilol = pygame.transform.scale(ui[0], (500,500))
lunginlol = pygame.transform.scale(lungin[0], (250,250))
tree = pygame.transform.scale(location2[3],(100,100))
tree2 = pygame.transform.scale(location2[2],(120,120))
tree3 = pygame.transform.scale(location2[4],(150,150))
mapa = pygame.transform.scale(location2[0],(1920,1080))
domlungina = pygame.transform.scale(location2[1],(350,350))
player = pygame.transform.scale(mishahodit[0],(int(player_size), player_size))
player_x = 1800
player_y = 980
player_speed = 3
player_rect = player.get_rect()
hero_image_number = 0
player_pos = [player_x, player_y]
clock = pygame.time.Clock()
schitat = 0
text1 = myfont.render('Ку, это я - малунгин', False, (0, 0, 0))
text2 = myfont.render('ты от полиции?', False, (0, 0, 0))
text3 = myfont.render('ну на тебе значит ключ от мальгина',False,(0,0,0))
text4 = myfont.render('Пойти к мальгину?',False,(0,0,0))
text5 = myfont.render('Нажмите  пробел чтобы продолжить',False,(0,0,0))
text6 = myfont.render('', False, (255,0,255))
def dialog():
    screen.blit(lunginlol, (200,100))
    screen.blit(text1, (500,150))
    screen.blit(text2, (500,250))
    screen.blit(text3, (200,350))
    screen.blit(text4, (200,600))
    screen.blit(text4, (200,600))
    screen.blit(text5, (650,750))
    kluch = 1
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Получение текущей позиции курсора мыши
    mouse_pos = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        player_x += player_speed
        schitat += 1
    if keys[pygame.K_a]:
        player_x -= player_speed
        hero_image_number += 1
        schitat += 1
    if keys[pygame.K_s]:
        player_y += player_speed
        hero_image_number += 1
        schitat += 1
    if keys[pygame.K_w]:
        player_y -= player_speed
        hero_image_number += 1
        schitat += 1
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
    if keys[pygame.K_SPACE]:
        subprocess.call(['python', 'end.py'])
        pygame.quit()
        sys.exit()
    else:
        hero_image_number = 0
    if schitat >= 0 and schitat <= 19:
        hero_image_number = 1
    elif schitat >= 20 and schitat <= 39:
        hero_image_number = 2
    elif schitat >=40 and schitat <= 60:
        hero_image_number = 0
        schitat = 0
    else:
        hero_image_number = 0
    if keys[pygame.K_SPACE]:
        blackscreen()
    screen.blit(mapa, (0, 0))
    #screen.blit(mishamaliginidle,(250,225))
    if player_x <= 1929 and player_y >=1069:
        player_y = player_y - (player_speed+10)
    if player_x <= 0 and player_y <= 1089:
        player_x = player_x + (player_speed+10)
    if player_x >=1929 and player_y <= 1089:
        player_x = player_x - (player_speed+1)
    if player_x >= 1180 and player_x <= 1555 and player_y >= 130 and player_y <= 445:
        dialog()
    screen.blit(tree, (1500,800))
    screen.blit(domlungina, (1200, 100))
    #поворот перса
    angle = math.atan2(mouse_pos[1] - player_y, mouse_pos[0] - player_x) * 180 / math.pi
    rotated_misha = pygame.transform.rotate(mishahodit[hero_image_number], -angle-90)
    asd = (player_x - rotated_misha.get_width()/2, player_y - rotated_misha.get_height()/2)
    screen.blit(rotated_misha, asd)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()