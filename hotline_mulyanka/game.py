import pygame, sys, random, os, subprocess
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
menu_pic = [
    pygame.image.load('./data/textures/mainmenu/play.png'),
    pygame.image.load('./data/textures/mainmenu/backgroundmenu.png'),
    pygame.image.load('./data/textures/mainmenu/quit.png'),
    pygame.image.load('./data/textures/mainmenu/about.png'),
    pygame.image.load('./data/textures/mainmenu/aboutlol.png')  
]
location1 = [
    pygame.image.load('./data/textures/resources/car.png'),
    pygame.image.load('./data/textures/resources/carmihi.png'),
    pygame.image.load('./data/textures/resources/Dom.png'),
    pygame.image.load('./data/textures/resources/map1.png'),
    pygame.image.load('./data/textures/resources/nezahobit.png'),
    pygame.image.load('./data/textures/resources/rain.png'),
    pygame.image.load('./data/textures/resources/zabor.png'), 
]
misha = [
    #malgin
    pygame.image.load('./data/textures/mihuyek/malgin/malginumer.png'),
    pygame.image.load('./data/textures/mihuyek/malgin/maliginleftudar.png'),
    pygame.image.load('./data/textures/mihuyek/malgin/maliginrightudar.png'),
    pygame.image.load('./data/textures/mihuyek/malgin/maliginlevo.png'),
    pygame.image.load('./data/textures/mihuyek/malgin/maliginpravo.png'),
    pygame.image.load('./data/textures/mihuyek/malgin/maliginidle.png'),
    #maligin
    pygame.image.load('./data/textures/mihuyek/maligin/maliginumer.png'),#умер 
    pygame.image.load('./data/textures/mihuyek/maligin/maliginumer2.png'),#умер 2
    pygame.image.load('./data/textures/mihuyek/maligin/mishaidle.png'),#стоит
    pygame.image.load('./data/textures/mihuyek/maligin/mishaleftudar.png'),#удар слева
    pygame.image.load('./data/textures/mihuyek/maligin/misharightudar.png'),#удар справа
    pygame.image.load('./data/textures/mihuyek/maligin/mishapravo.png'),#шаг правой ноги
    pygame.image.load('./data/textures/mihuyek/maligin/mishalevo.png'),#шаг левой ноги
]
mishass = pygame.transform.scale(misha[0],(600,250))
bckgrd_mainmenu = pygame.transform.scale( menu_pic[1], (1920, 1080 ))
playbtn = pygame.transform.scale(menu_pic[0],(600,250))
quitbtn = pygame.transform.scale(menu_pic[2], (600,250))
aboutbtn = pygame.transform.scale(menu_pic[3], (600,250))
aboutmf = pygame.transform.scale(menu_pic[4], (1000,600))
show = True
keys = pygame.key.get_pressed()
screen.blit(aboutmf, (500, 300))
screen.blit(bckgrd_mainmenu, (0,0))
screen.blit(playbtn, (1200,500))
screen.blit(aboutbtn, (1200,650))
screen.blit(quitbtn, (1200,800))
#rect = bckgrd_mainmenu.get_rect()
texttgdelali = myfont.render('(TG) делали krol229', False, (0, 0, 0))
text2 = myfont.render('   FullSpeedToTotalMayhem', False, (0, 0, 0))
text3 = myfont.render('   Kajura6', False, (0, 0, 0))
text4 = myfont.render('   TATAPSTAN', False, (0, 0, 0))
textquit = myfont.render('Выйти', False, (255, 0, 255))
def vosstanovlenie():
    aboutmf = pygame.transform.scale(0, (0,0))
def about():
    screen.blit(bckgrd_mainmenu, (0,0))
    screen.blit(aboutmf, (400, 300))
    screen.blit(texttgdelali, (500,400))#тг делали
    screen.blit(text2, (500,500))#максон
    screen.blit(text3, (500,600))#темыч
    screen.blit(text4, (500,700))#анит
    screen.blit(textquit, (1000,900)) #выйти
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if 1000<= mouse_pos[0] <= 1000 + 100 and \
                900 <= mouse_pos[1] <= 900 + 200:
                    vosstanovlenie()
def menu():
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if 1200 <= mouse_pos[0] <= 1200 + 600 and \
                500 <= mouse_pos[1] <= 500 + 250:
                subprocess.call(['python', 'location1.py'])
                pygame.quit()
                sys.exit()
            if 1200 <= mouse_pos[0] <= 1200 + 600 and \
                650 <= mouse_pos[1] <= 650 + 250:
                about()
            if 1200 <= mouse_pos[0] <= 1200 + 600 and \
                800 <= mouse_pos[1] <= 800 + 250:
                pygame.quit()
                sys.exit()
clock = pygame.time.Clock()
while running:
    show = True
    menu()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    clock.tick(50)
pygame.quit()
sys.exit()