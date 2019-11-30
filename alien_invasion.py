import os
import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from statusbar import StatusBar
from pygame.sprite import Group
from gamestatus import GameStatus
from button import Button
from screen_msg import ScreenMsg


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
    status = GameStatus(settings)
    statusbar = StatusBar(screen, ship.centerx, ship.centery, settings, 0, len(aliens), status.ship_limit)
    play_button = Button(screen, '开始游戏')
    quit_button = Button(screen, '退出游戏(Q)')
    gf.set_btn_pos(quit_button, screen.get_rect().center, (0, 80))
    msg = ScreenMsg(screen, '游戏结束')

    while True:
        gf.check_events(screen, ship, aliens, settings, bullets, play_button, status, quit_button)
        gf.check_game_status(status)
        if status.game_alive == 2:
            gf.check_game_hit(ship, aliens, bullets, status, settings.screen_height)
            ship.update()
            gf.update_bullets(bullets)
            gf.update_aliens(aliens, bullets, screen, settings, status.game_alive)
            statusbar.update(ship.centerx, ship.centery, len(bullets), len(aliens), status.ship_limit)
            gf.check_fire(bullets, aliens)

        gf.update_screen(settings, screen, ship, statusbar, bullets, aliens, play_button, quit_button, status, msg)


run_game()
