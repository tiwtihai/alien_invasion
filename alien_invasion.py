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
    game_settings = Settings()
    os.environ["SDL_VIDEO_WINDOW_POS"] = "%d, %d" % (game_settings.screen_left, game_settings.screen_top)
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(screen, game_settings.ship_speed_factor)
    statusbar = StatusBar(screen, ship.centerx, ship.centery, game_settings, 0)
    bullets = Group()
    alien = Alien(screen, game_settings)

    while True:
        gf.check_events(screen, ship, game_settings, bullets)
        ship.update()
        # bullet.update()
        bullets.update()
        statusbar.update(ship.centerx, ship.centery, len(bullets))
        alien.update()
        gf.update_screen(game_settings, screen, ship, statusbar, bullets, alien)
        gf.destory_bullets(bullets)


run_game()
