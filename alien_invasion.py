import os

import pygame
from pygame.sprite import Group

import game_functions as gf
from buttons import Buttons
from game_info import GameInfo
from game_status import GameStatus
from screen_pop_msg import ScreenPopMsg
from settings import Settings
from ship import Ship


def run_game():
    pygame.init()
    settings = Settings()
    os.environ["SDL_VIDEO_WINDOW_POS"] = "%d, %d" % (settings.screen_left, settings.screen_top)
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption('外星人入侵')
    ship = Ship(screen, settings.ship_speed_factor)
    bullets = Group()
    aliens = Group()
    gf.creat_aliens(aliens, screen, settings)
    status = GameStatus(settings)
    game_info = GameInfo(screen, ship, settings, 0, len(aliens), status)
    buttons=Buttons(screen)
    pop_msg = ScreenPopMsg(screen)

    while True:
        gf.check_events(screen, ship, aliens, settings, bullets, buttons, status, game_info)
        gf.check_game_status(status)
        if status.game_alive == 2:
            gf.check_game_hit(ship, aliens, bullets, status, settings.screen_height, game_info)
            ship.update()
            gf.update_bullets(bullets)
            gf.update_aliens(aliens, bullets, screen, settings, status.game_alive)
            game_info.prep_statusbar(len(bullets), len(aliens))
            gf.check_fire(bullets, aliens, settings, status, game_info)

        gf.update_screen(settings, screen, ship, game_info, bullets, aliens, buttons, status, pop_msg)


run_game()
