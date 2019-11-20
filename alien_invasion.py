import sys
import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from statusbar import StausBar

def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screnn_height))
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(screen, game_settings.ship_speed_factor)
    statusbar=StausBar(screen)
    while True:
        gf.check_events(ship)
        ship.update()
        statusbar.printtext()
        gf.update_screen(game_settings, screen, ship)


run_game()
