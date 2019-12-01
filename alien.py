import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, screen, settings):
        super().__init__()
        self.screen = screen
        self.factor = settings.alien_speed_factor
        self.image = pygame.image.load("images/alien.png")
        self.screen_rect = screen.get_rect()
        self.rect = self.image.get_rect()
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        self.moving_lr = settings.aliens_move_lr
        self.drop_interval = settings.alien_drop_interval if settings.alien_drop_interval < self.rect.height else self.rect.height

    def update(self, check_edge):
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        if check_edge:
            self.moving_lr *= -1
            self.y += self.drop_interval
        self.x += self.factor * self.moving_lr
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        # print('%s:x->%d,y->%d' % (str(id(self)), self.rect.x, self.rect.y))
