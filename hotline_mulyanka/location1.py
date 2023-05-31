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
    pygame.image.load('./data/textures/resources/car.png'),
    pygame.image.load('./data/textures/resources/carmihi.png'),
    pygame.image.load('./data/textures/resources/Dom.png'),
    pygame.image.load('./data/textures/resources/map1.png'),#3
    pygame.image.load('./data/textures/resources/nezahobit.png'),
    pygame.image.load('./data/textures/resources/rain.png'),
    pygame.image.load('./data/textures/resources/zabor.png'), 
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
player = pygame.transform.scale(mishahodit[0],(100,100))
mapa = pygame.transform.scale(location1[3],(1920,1080))
player_x = 1800
player_y = 980
player_speed = 7
player_rect = player.get_rect()
player_size = 20
hero_image_number = 0
player_pos = [player_x, player_y]
clock = pygame.time.Clock()
#position = [player_x, player_y]
schitat = 0
def rotate(self):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    rel_x, rel_y = mouse_x - self.x, mouse_y - self.y
    angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
    self.image = pygame.transform.rotate(self.original_image, int(angle))
    self.rect = self.image.get_rect(center=self.position)
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
    #поворот перса
    
    angle = math.atan2(mouse_pos[1] - player_y, mouse_pos[0] - player_x) * 180 / math.pi
    rotated_misha = pygame.transform.rotate(mishahodit[hero_image_number], -angle-90)
    screen.blit(mapa, (0, 0))
    asd = (player_x - rotated_misha.get_width()/2, player_y - rotated_misha.get_height()/2)
    screen.blit(rotated_misha, asd)
    pygame.display.flip()
    clock.tick(50)
pygame.quit()
sys.exit()