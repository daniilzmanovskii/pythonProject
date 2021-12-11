import pygame

pygame.init()
win = pygame.display.set_mode((256, 256))

pygame.display.set_caption('Star Dodge')

bg = pygame.image.load('darkPurple.png')
playerStand = pygame.image.load('playerShip1_blue.png')

x = 150
y = 175
width = 99
height = 75
speed = 10

def drawWindow():
    win.blit(bg, (0, 0))
    win.blit(playerStand, (x, y))
    pygame.display.update()

run = True
while run:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 15:
        x -= speed
    if keys[pygame.K_RIGHT] and x < 241 - width:
        x += speed

    drawWindow()

pygame.quit()

