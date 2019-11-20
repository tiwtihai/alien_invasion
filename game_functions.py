import sys
import pygame
from bullet import Bullet
import datetime


def check_events(screen, ship, game_settings, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            if event.key == pygame.K_LEFT:
                ship.moving_left = True
            if event.key == pygame.K_UP:
                ship.moving_up = True
            if event.key == pygame.K_DOWN:
                ship.moving_down = True
            if event.key == pygame.K_f:
                new_bullet = Bullet(screen, ship, game_settings)
                bullets.add(new_bullet)
            if event.key == pygame.K_q:
                sys.exit()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            if event.key == pygame.K_LEFT:
                ship.moving_left = False
            if event.key == pygame.K_UP:
                ship.moving_up = False
            if event.key == pygame.K_DOWN:
                ship.moving_down = False


def destory_bullets(bullets):
    for bullet in bullets.copy():
        if bullet.y < 0:
            bullets.remove(bullet)


def update_screen(game_settings, screen, ship, statusbar, bullets,alien):
    screen.fill(game_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.launch()
    ship.blitme()
    alien.blitme()
    statusbar.print_text()
    pygame.display.flip()
