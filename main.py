import sys
import pygame
from Meteor import Meteor
import pygame_menu

pygame.init()

display_width = 800
display_height = 600
menu_width = 800
menu_height = 600

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Star Dodge')
fon1 = pygame.image.load('darkPurple.png')
player1 = pygame.image.load('playerShip1_red.png')

width = 60
height = 100
x = display_width // 2 - 50
y = display_height - height - 50

c_x = display_width - 50
c_y = display_height - 20 - 100
c_w = 20
c_h = 70

meteors = pygame.sprite.Group

meteors.add(Meteor(display_width // 2, 10, 'BBrown.png'))
#meteors.add(Meteor(display_width - 50, 5, 'MGrey.png'))
#meteors.add(Meteor(display_width - 400, 7, 'MBrown.png'))
#meteors.add(Meteor(display_width, 9, 'BGrey.png'))


def terminate():
    pygame.quit()
    sys.exit()


def start_menu(theme=pygame_menu.themes.THEME_BLUE):
    menu = pygame_menu.Menu('Star Dodge', menu_width, menu_height, theme=theme)
    menu.add.button('PLAY', start_game)
    menu.add.button('EXIT', pygame_menu.events.EXIT)
    menu.mainloop(display)


font = pygame.font.SysFont('microsofttaile', 32)
follow = font.render('Pause! Press ENTER to continue', 1, (173, 255, 47))


def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.blit(follow, (180, 270))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            paused = False

        pygame.display.update()


cactus_arr_left = []
cactus_arr_right = []


run = True


font1 = pygame.font.SysFont('microsofttaile', 32)
follow1 = font1.render('Game Over! Press ENTER to play  again. Escape to exit!', 1, (173, 255, 47))


def game_over():
    stopped = True
    while stopped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.blit(follow1, (20, 270))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            return True
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            quit()

        pygame.display.update()


def start_game():
    global x, y
    while run:
        pygame.time.delay(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x > 15:
            x -= 15
        if keys[pygame.K_RIGHT] and x < 785 - width:
            x += 15
        if keys[pygame.K_DOWN]:
            y += 10
        if keys[pygame.K_UP]:
            y -= 10
        pressed = pygame.mouse.get_pressed()
        if pressed[1]:
            game_over()
        if keys[pygame.K_ESCAPE]:
            pause()

        display.blit(fon1, (0, 0))
        display.blit(player1, (x, y))
        meteors.draw(display)
        pygame.display.update()

        meteors.update(display_height)


start_menu()