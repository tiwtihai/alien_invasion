import sys, os
import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from statusbar import StatusBar


def run_game():
    pygame.init()
    game_settings = Settings()
    os.environ["SDL_VIDEO_WINDOW_POS"] = "%d, %d" % (game_settings.screen_left, game_settings.screen_top)
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(screen, game_settings.ship_speed_factor)
    statusbar = StatusBar(screen, ship.centerx, ship.centery,game_settings)
    while True:
        gf.check_events(ship)
        ship.update()
        statusbar.update(ship.centerx, ship.centery, game_settings)
        gf.update_screen(game_settings, screen, ship, statusbar)


run_game()
