import pygame
import sys


class Alien:
    def __init__(self, screen, game_settings):
        self.screen = screen
        self.factor = game_settings.alien_factor
        self.image = pygame.image.load("images/alien.bmp")
        self.screen_rect = screen.get_rect()
        self.rect = self.image.get_rect()
        self.y = float(self.rect.y)
        self.rect.top = self.screen_rect.top + 10
        self.rect.left = self.screen_rect.left + 10

    def update(self):
        self.y += self.factor
        self.rect.y = self.y

    #def destroy(self):


    def blitme(self):
        self.screen.blit(self.image, self.rect)
