import pygame


class Ship:
    def __init__(self, screen, ship_speed_factor):
        self.screen_rect = screen.get_rect()
        self.screen = screen
        self.ship_speed_factor = ship_speed_factor
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()

        self.centerx = float(self.screen_rect.centerx)
        self.centery = float(self.screen_rect.bottom - self.rect.height / 2)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right is True and self.rect.right < self.screen_rect.right:
            self.centerx += self.ship_speed_factor
        if self.moving_left is True and self.rect.left > self.screen_rect.left:
            self.centerx -= self.ship_speed_factor
        if self.moving_up is True and self.rect.top > self.screen_rect.top:
            self.centery -= self.ship_speed_factor
        if self.moving_down is True and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ship_speed_factor
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        self.screen.blit(self.image, self.rect)
