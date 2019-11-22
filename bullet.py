import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, screen, ship, settings):
        super().__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)
        self.factor = settings.bullet_factor
        self.color = settings.bullet_color

    def update(self):
        self.y -= self.factor
        self.rect.y = self.y

    def launch(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
