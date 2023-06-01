import pygame, sys, random, math
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
player_size = 1
#sad = pygame.transform.scale(player_pic, (int(player_size * 1.25), player_size))
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
player_speed = 7
player_rect = player.get_rect()
hero_image_number = 0
player_pos = [player_x, player_y]
clock = pygame.time.Clock()
schitat = 0
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
    screen.blit(dom, (31,642))
    screen.blit(dom1, (435,491))
    screen.blit(dommalgin, (1459, 390))
    screen.blit(carmiha, (1350,887))
    screen.blit(zabormihi, (1440, 180))
    screen.blit(car, (1070, 280))
    screen.blit(nezahodit, (550, 230))
    
    if player_x <= 1919 and player_y >=1079:
        player_y = player_y - (player_speed+1)
    if player_x <= 0 and player_y <= 1079:
        player_x = player_x + (player_speed+1)
    if player_x >=1929 and player_y <= 1089:
        player_x = player_x - (player_speed+1)
    #поворот перса
    angle = math.atan2(mouse_pos[1] - player_y, mouse_pos[0] - player_x) * 180 / math.pi
    rotated_misha = pygame.transform.rotate(mishahodit[hero_image_number], -angle-90)
    asd = (player_x - rotated_misha.get_width()/2, player_y - rotated_misha.get_height()/2)
    screen.blit(rotated_misha, asd)
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()
