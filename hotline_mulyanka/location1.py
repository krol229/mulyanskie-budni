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
location1 = [
    pygame.image.load('./data/textures/resources/car.png'),#0
    pygame.image.load('./data/textures/resources/carmihi.png'),#1
    pygame.image.load('./data/textures/resources/dom.png'),#2
    pygame.image.load('./data/textures/resources/map1.png'),#3
    pygame.image.load('./data/textures/resources/nezahobit.png'),#4
    pygame.image.load('./data/textures/resources/rain.png'),#5
    pygame.image.load('./data/textures/resources/zabor.png'),#6
    pygame.image.load('./data/textures/resources/malginhome.png'),#7 
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
mishinhooksprava = pygame.transform.scale(misha[2],(int(player_size), player_size))
mishinhooksleva = pygame.transform.scale(misha[1],(int(player_size), player_size))
#sad = pygame.transform.scale(player_pic, (int(player_size * 1.25), player_size))
mishamaliginidle = pygame.transform.scale(misha[5],(100,100))
player = pygame.transform.scale(mishahodit[0],(int(player_size), player_size))
mapa = pygame.transform.scale(location1[3],(1920,1080))
dom = pygame.transform.scale(location1[2], (200,200))
dom1 = pygame.transform.scale(location1[2], (200,200))
dommalgin = pygame.transform.scale((location1[7]),(380,380))
carmiha = pygame.transform.scale((location1[1]),(300,300))
zabormihi = pygame.transform.scale((location1[6]),(500, 500))
car = pygame.transform.scale((location1 [0]), (250, 300))
nezahodit = pygame.transform.scale((location1[4]), (1000, 400))
player_x = 1800
player_y = 980
player_speed = 10
player_rect = player.get_rect()
hero_image_number = 0
player_pos = [player_x, player_y]
clock = pygame.time.Clock()
schitat = 0
text1 = myfont.render('Привет тут был малыгин... снова...', False, (0, 0, 0))
text2 = myfont.render('найди лунгина и возьми ключ от дома', False, (0, 0, 0))
text3 = myfont.render('Пойти через реку?',False,(0,0,0))
text4 = myfont.render('Да',False,(0,0,0))
def dialog():
    screen.blit(text1, (1000,150))
    screen.blit(text2, (900,250))
    screen.blit(text3, (500,900))
    screen.blit(text4, (500,1000))
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
    else:
        hero_image_number = 0
    if keys[pygame.K_SPACE]:
        subprocess.call(['python', 'location2.py'])
        pygame.quit()
        sys.exit()
    if schitat >= 0 and schitat <= 19:
        hero_image_number = 1
    elif schitat >= 20 and schitat <= 39:
        hero_image_number = 2
    elif schitat >=40 and schitat <= 60:
        hero_image_number = 0
        schitat = 0
    else:
        hero_image_number = 0
    screen.blit(mapa, (0, 0))
    screen.blit(dom, (30,347))
    screen.blit(dom,(31,642))
    screen.blit(dom1, (435,491))
    screen.blit(dommalgin, (1459, 390))
    screen.blit(carmiha, (1350,887))
    screen.blit(zabormihi, (1440, 180))
    screen.blit(car, (1070, 280))
    screen.blit(nezahodit, (550, 230))
    #screen.blit(mishamaliginidle,(250,225))
    if player_x <= 1929 and player_y >=1069:
        player_y = player_y - (player_speed+10)
    if player_x <= 0 and player_y <= 1089:
        player_x = player_x + (player_speed+10)
    if player_x >=1929 and player_y <= 1089:
        player_x = player_x - (player_speed+1)
    if player_x <= 1650 and player_x >= 1355 and player_y >= 975 and player_y <= 1850:
        player_y -= player_speed
    if player_x >= 435 and player_x <= 650 and player_y >= 491 and player_y <= 625:
        player_y -= player_speed
    if player_x >= 30 and player_x <= 235 and player_y >= 347 and player_y <= 500:
        player_x += player_speed
    if player_x >= 30 and player_x <= 235 and player_y >= 642 and player_y <= 808:
        player_x += player_speed
    if player_x >= 1555 and player_x <= 1725 and player_y >= 545 and player_y <= 680:
        player_y += player_speed
    if player_x >= 1588 and player_x <= 1591 and player_y >= 280 and player_y <= 550:
        player_x -= player_speed
    if player_x >= 2 and player_x <= 1980 and player_y <= 260 and player_y >= 250:
        player_y += player_speed
    if player_x >= 1120 and player_x <= 1263 and player_y >= 300 and player_y <= 508:
        dialog()
    #поворот перса
    angle = math.atan2(mouse_pos[1] - player_y, mouse_pos[0] - player_x) * 180 / math.pi
    rotated_misha = pygame.transform.rotate(mishahodit[hero_image_number], -angle-90)
    asd = (player_x - rotated_misha.get_width()/2, player_y - rotated_misha.get_height()/2)
    screen.blit(rotated_misha, asd)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()