import pygame

pygame.init()
win = pygame.display.set_mode((800, 600))

pygame.display.set_caption('Star Dodge')

bg = pygame.image.load('darkPurple.png')
playerStand = pygame.image.load('playerShip1_blue.png')
meteorMB = pygame.image.load('MBrown.png')
meteorSB = pygame.image.load('SBrown.png')
meteorBB = pygame.image.load('BBrown.png')
meteorBG = pygame.image.load('BGrey.png')
meteorSG = pygame.image.load('SGrey.png')
meteorMG = pygame.image.load('MGrey.png')

x = 350
y = 480
width = 99
height = 75
speed = 10

MeteorBBMoveRight_size_x = 20
MeteorBBMoveRight_size_y = 0
MeteorBBMoveRight_position_x = 800 - 50
MeteorBBMoveRight_position_y = 600 - 550
MeteorBBMoveRight_speed_x = 8
MeteorBBMoveRight_speed_y = 10

MeteorSBMoveRight_size_x = 20
MeteorSBMoveRight_size_y = 0
MeteorSBMoveRight_size_x = 450 - 50
MeteorSBMoveRight_size_y = 600 - 480
MeteorSBMoveRight_speed_x = 12
MeteorSBMoveRight_speed_y = 10

MeteorMGMoveRight_size_x = 20
MeteorMGMoveRight_size_y = 0
MeteorMGMoveRight_position_x = 150 - 50
MeteorMGMoveRight_position_y = 400 - 40
MeteorMGMoveRight_speed_x = 9
MeteorMGMoveRight_speed_y = 7

MeteorBGMoveRight_size_x = 20
MeteorBGMoveRight_size_y = 0
MeteorBGMoveRight_position_x = 80
MeteorBGMoveRight_position_y = 50
MeteorBGMoveRight_speed_x = 11
MeteorBGMoveRight_speed_y = 9

MeteorMBMoveRight_size_x = 20
MeteorMBMoveRight_size_y = 0
MeteorMBMoveRight_position_x = 400
MeteorMBMoveRight_position_y = 200
MeteorMBMoveRight_speed_x = 8
MeteorMBMoveRight_speed_y = 15

def moveCactusRight1():
    global MeteorMBMoveRight_size_y, MeteorMBMoveRight_position_y, MeteorMBMoveRight_position_x, MeteorMBMoveRight_size_x

    if MeteorMBMoveRight_position_x <= MeteorBGMoveRight_size_x + 800:
        MeteorMBMoveRight_position_x += 8
    else:
        MeteorMBMoveRight_position_x = 50

    if MeteorMBMoveRight_position_y >= MeteorBGMoveRight_size_y - 50 and (MeteorMBMoveRight_position_y < 650):
        MeteorMBMoveRight_position_y += 15
    else:
        MeteorMBMoveRight_position_y = 0

def moveCactusRight():
    global MeteorBGMoveRight_size_y, MeteorBGMoveRight_position_y, MeteorBGMoveRight_position_x, MeteorBGMoveRight_size_x

    if MeteorBGMoveRight_position_x <= MeteorBGMoveRight_size_x + 800:
        MeteorBGMoveRight_position_x += 11
    else:
        MeteorBGMoveRight_position_x = 50

    if MeteorBGMoveRight_position_y >= MeteorBGMoveRight_size_y - 50 and (MeteorBGMoveRight_position_y < 650):
        MeteorBGMoveRight_position_y += 9
    else:
        MeteorBGMoveRight_position_y = 0

def moveCactusLeft():
    global MeteorBBMoveRight_size_y, MeteorBBMoveRight_position_y, MeteorBBMoveRight_position_x, MeteorBBMoveRight_size_x

    if MeteorBBMoveRight_position_x >= MeteorBBMoveRight_size_x:
        MeteorBBMoveRight_position_x -= MeteorBBMoveRight_speed_x
    else:
        MeteorBBMoveRight_position_x = 800 - 50

    if MeteorBBMoveRight_position_y >= MeteorBBMoveRight_size_y - 50 and (MeteorBBMoveRight_position_y < 650):
        MeteorBBMoveRight_position_y += MeteorBBMoveRight_speed_y
    else:
        MeteorBBMoveRight_position_y = 0

def moveCactusLeft1():
    global MeteorMGMoveRight_size_y, MeteorSBMoveRight_size_y, MeteorSBMoveRight_size_x, MeteorMGMoveRight_size_x

    if MeteorSBMoveRight_size_x >= MeteorMGMoveRight_size_x:
        MeteorSBMoveRight_size_x -= 12
    else:
        MeteorSBMoveRight_size_x = 800 - 50

    if MeteorSBMoveRight_size_y >= MeteorMGMoveRight_size_y - 50 and (MeteorSBMoveRight_size_y < 650):
        MeteorSBMoveRight_size_y += 10
    else:
        MeteorSBMoveRight_size_y = 0

def moveCactusLeft2():
    global MeteorMGMoveRight_size_y, MeteorMGMoveRight_position_y, MeteorMGMoveRight_position_x, MeteorMGMoveRight_size_x

    if MeteorMGMoveRight_position_x >= MeteorMGMoveRight_size_x:
        MeteorMGMoveRight_position_x -= 9
    else:
        MeteorMGMoveRight_position_x = 800 - 50

    if MeteorMGMoveRight_position_y >= MeteorMGMoveRight_size_y - 50 and (MeteorMGMoveRight_position_y < 650):
        MeteorMGMoveRight_position_y += 7
    else:
        MeteorMGMoveRight_position_y = 0


font = pygame.font.SysFont('microsofttaile', 32)
follow = font.render('Pause! Press ENTER to continue', 1, (173, 255, 47))

def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        win.blit(follow, (180, 270))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            paused = False

        pygame.display.update()


def drawWindow():
    win.blit(bg, (0, 0))
    win.blit(playerStand, (x, y))
    win.blit(meteorBB, (MeteorBBMoveRight_position_x, MeteorBBMoveRight_position_y))
    win.blit(meteorSB, (MeteorSBMoveRight_size_x, MeteorSBMoveRight_size_y))
    win.blit(meteorMG, (MeteorMGMoveRight_position_x, MeteorMGMoveRight_position_y))
    win.blit(meteorBG, (MeteorBGMoveRight_position_x, MeteorBGMoveRight_position_y))
    win.blit(meteorMB, (MeteorMBMoveRight_position_x, MeteorMBMoveRight_position_y))
    pygame.display.update()

run = True
while run:
    pygame.time.delay(35)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 15:
        x -= speed
    if keys[pygame.K_RIGHT] and x < 785 - width:
        x += speed
    if keys[pygame.K_ESCAPE]:
        pause()

    moveCactusRight1()
    moveCactusRight()
    moveCactusLeft2()
    moveCactusLeft1()
    moveCactusLeft()
    drawWindow()



pygame.quit()

