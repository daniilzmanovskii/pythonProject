import sys
import pygame
from Meteor import Meteor
from random import randint
import pygame_menu

pygame.init()

display_width = 800
display_height = 600
menu_width = 800
menu_height = 600

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Star Dodge')
fon1 = pygame.image.load('darkPurple.png')
player1 = pygame.image.load('Foguete-pixelizado-Png.png').convert_alpha()
player_rect = player1.get_rect(centerx=display_width//2, bottom=display_height-5)
pygame.time.set_timer(pygame.USEREVENT, 300)

width = 60
height = 100
x = display_width // 2 - 50
y = display_height - height - 50
speed = 15

c_x = display_width - 50
c_y = display_height - 20 - 100
c_w = 20
c_h = 70

all_sprites = pygame.sprite.Group()
meteors = pygame.sprite.Group()
all_sprites.add(meteors)

meteor_images = ['BBrown.png', 'BGrey.png', 'MBrown.png', 'MGrey.png', 'SBrown.png', 'SGrey.png']
meteor_surf = [pygame.image.load(path).convert_alpha() for path in meteor_images]


def create_meteor(group):
    indx = randint(0, len(meteor_surf) - 1)
    x = randint(100, display_width - 100)
    speed = randint(6, 16)

    return Meteor(x, speed, meteor_surf[indx], group)


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


run = True
create_meteor(meteors)


def collide_meteors():
    for meteor in meteors:
        if player_rect.collidepoint(meteor.rect.center):
            game_over()


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
            elif event.type == pygame.USEREVENT:
                create_meteor(meteors)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_rect.x -= speed
            if player_rect.x < 0:
                player_rect.x = 0
        elif keys[pygame.K_RIGHT]:
            player_rect.x += speed
            if player_rect.x > 800 - 55:
                player_rect.x = 800 - 55
        elif keys[pygame.K_UP]:
            player_rect.y -= speed
            if player_rect.y < 0:
                player_rect.y = 0
        elif keys[pygame.K_DOWN]:
            player_rect.y += speed
            if player_rect.y > 600 - 77:
                player_rect.y = 600 - 77


        pressed = pygame.mouse.get_pressed()
        if pressed[1]:
            game_over()
        if keys[pygame.K_ESCAPE]:
            pause()

        collide_meteors()
        display.blit(fon1, (0, 0))
        display.blit(player1, (player_rect))
        meteors.draw(display)
        pygame.display.update()

        meteors.update(display_height)


start_menu()