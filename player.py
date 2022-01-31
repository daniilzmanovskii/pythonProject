import pygame

width = 60
height = 100
x = 800 // 2 - 50
y = 600 - height - 50


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(0, 255, 0)
        self.rect = self.image.get_rect()
        self.rect.centerx = 800 / 2
        self.rect.bottom = 600 - 10
        self.speedx = 0

  def update(self):
      global x, y
      keys = pygame.key.get_pressed()
      if keys[pygame.K_LEFT] and x > 15:
          x -= 15
      if keys[pygame.K_RIGHT] and x < 785 - width:
          x += 15
      if keys[pygame.K_DOWN] and y < 560 - height:
          y += 10
      if keys[pygame.K_UP] and y > 30:
          y -= 10