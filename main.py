import random

import pygame

pygame.init()

display_width = 800
display_height = 600

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Star Dodge')
fon1 = pygame.image.load('darkPurple.png')
player1 = pygame.image.load('playerShip1_red.png')

width = 60
height = 100
x = display_width // 3
y = display_height - height - 100

c_x = display_width - 50
c_y = display_height - 20 - 100
c_w = 20
c_h = 70


class Cactus():
    def __init__(self, x1, y1, width1, height1, speed_x, speed_y, image):
        self.x = x1
        self.y = y1
        self.width = width1
        self.height = height1
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.image = image

    def move_left(self):
        display.blit(self.image, (self.x, self.y))
        if self.x >= -self.width:
            self.x -= self.speed_x
        else:
            self.x = display_width - 50

        if self.y >= self.height - 150 and (self.y < 650):
            self.y += self.speed_y
        else:
            self.y = 0

    def move_right(self):
        display.blit(self.image, (self.x, self.y))
        if self.x <= -self.width + 800:
            self.x += self.speed_x
        else:
            self.x = 50

        if self.y >= self.height - 120 and (self.y < 650):
            self.y += self.speed_y
        else:
            self.y = 0


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


width = 60
height = 100
x = display_width // 3
y = display_height - height - 30

c_x = display_width - 50
c_y = display_height - 170
c_w = 20
c_h = 70

cactus_arr_left = []
cactus_arr_right = []


def create_cactus_arr(array):
    array.append(Cactus(display_width - 50, display_height, 101, 84, 4, 5, pygame.image.load('BBrown.png')))
    array.append(Cactus(display_width - 500, display_height + 43, 43, 50, 3, 4, pygame.image.load('MBrown.png')))
    array.append(Cactus(display_width - 300, display_height + 100, 28, 28, 6, 4, pygame.image.load('SGrey.png')))


def draw_array(array):
    for cactus in array:
        cactus.move_left()


def create_cactus_arrR(array):
    array.append(Cactus(display_width, display_height, 120, 98, 6, 6, pygame.image.load('BGrey.png')))
    array.append(Cactus(display_width - 500, display_height + 50, 28, 28, 4, 7, pygame.image.load('SBrown.png')))
    array.append(Cactus(display_width - 300, display_height + 100, 45, 40, 5, 2, pygame.image.load('MGrey.png')))


def draw_arrayR(array):
    for cactus in array:
        cactus.move_right()


run = True
create_cactus_arr(cactus_arr_left)
create_cactus_arrR(cactus_arr_right)

while run:
    pygame.time.delay(35)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 15:
        x -= 15
    if keys[pygame.K_RIGHT] and x < 785 - width:
        x += 15
    if keys[pygame.K_ESCAPE]:
        pause()

    display.blit(fon1, (0, 0))
    draw_array(cactus_arr_left)
    draw_arrayR(cactus_arr_right)

    display.blit(player1, (x, y))
    pygame.display.update()
