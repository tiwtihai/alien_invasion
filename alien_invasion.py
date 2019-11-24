import sys, os
import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from statusbar import StatusBar
from pygame.sprite import Group
from alien import Alien


def run_game():
    pygame.init()
    settings = Settings()
    os.environ["SDL_VIDEO_WINDOW_POS"] = "%d, %d" % (settings.screen_left, settings.screen_top)
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(screen, settings.ship_speed_factor)
    bullets = Group()
    aliens = Group()
    gf.creat_aliens(aliens, screen, settings)
    statusbar = StatusBar(screen, ship.centerx, ship.centery, settings, 0, len(aliens))

    while True:
        gf.check_events(screen, ship, settings, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(aliens, settings.screen_width, settings.screen_height)
        statusbar.update(ship.centerx, ship.centery, len(bullets), len(aliens))
        gf.check_fire(bullets, aliens, screen, settings)
        # gf.check_gameover()
        gf.update_screen(settings, screen, ship, statusbar, bullets, aliens)


run_game()
