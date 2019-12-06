import sys
import time

import pygame

from alien import Alien
from bullet import Bullet


def check_events(screen, ship, aliens, settings, bullets, buttons, status, game_info):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status.save_record()
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
                new_bullet = Bullet(screen, ship, settings)
                bullets.add(new_bullet)
            if event.key == pygame.K_p:
                if status.game_alive == 2:
                    status.game_alive = 4
                elif status.game_alive == 4:
                    status.game_alive = 2
            if event.key == pygame.K_s:
                play_button_click(status, settings, game_info, ship, aliens, bullets)
            if event.key == pygame.K_q:
                status.save_record()
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

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if check_button_click(mouse_x, mouse_y, buttons.play_button_rect):
                play_button_click(status, settings, game_info, ship, aliens, bullets)
            if check_button_click(mouse_x, mouse_y, buttons.quit_button_rect):
                status.save_record()
                sys.exit()


def update_screen(settings, screen, ship, game_info, bullets, aliens, buttons, status, pop_msg):
    screen.fill(settings.bg_color)
    for alien in aliens.sprites():
        alien.blitme()
    for bullet in bullets.sprites():
        bullet.launch()
    ship.blitme()
    if status.game_alive == 1 or status.game_alive == 3:
        buttons.show_play_button()
    if status.game_alive == 3:
        buttons.show_quit_button()
        pop_msg.update_msg('游戏结束')
        pop_msg.show_screen_msg()
    if status.game_alive == 4:
        pop_msg.update_msg('游戏暂停(P)')
        pop_msg.show_screen_msg()
    game_info.show_game_info()
    pygame.display.flip()


def creat_aliens(aliens, screen, settings):
    alien_model = Alien(screen, settings)
    alien_width = alien_model.rect.width
    alien_height = alien_model.rect.height
    screen_width = settings.screen_width

    aliens_rows = settings.aliens_rows
    aliens_rows_max = int(screen_width / alien_width)
    if aliens_rows > aliens_rows_max:
        aliens_rows = aliens_rows_max
    aliens_space_x = (screen_width - alien_width *
                      aliens_rows) / (aliens_rows + 1)

    aliens_lines = settings.aliens_lines
    aliens_space_y = alien_height / 2

    for line in range(1, aliens_lines + 1):
        for row in range(1, aliens_rows + 1):
            alien = Alien(screen, settings)
            alien.rect.x = aliens_space_x * row + alien_width * (row - 1)
            alien.rect.y = -(aliens_space_y * (line - 1) +
                             alien_height * line) + alien_height
            aliens.add(alien)


def check_edge(aliens, screen_width):
    for alien in aliens.sprites():
        if alien.rect.right >= screen_width or alien.rect.left <= 0:
            return True
    return False


def update_bullets(bullets):
    bullets.update()
    destroy_bullets(bullets)


def update_aliens(aliens, bullets, screen, settings, game_alive):
    aliens.update(check_edge(aliens, settings.screen_width))
    if len(aliens) == 0 and game_alive == 2:
        bullets.empty()
        creat_aliens(aliens, screen, settings)


def check_fire(bullets, aliens, settings, status, game_info):
    if pygame.sprite.groupcollide(bullets, aliens, True, True):
        status.score += settings.alien_point
        game_info.prep_score()
        if status.high_score <= status.score:
            status.high_score = status.score
            game_info.prep_high_score()
        if len(aliens) <= 0:
            settings.increase_speed()
            status.level += 1
            if status.high_level < status.level:
                status.high_level = status.level
            game_info.prep_level()
        return True
    return False


def check_game_status(status):
    if status.game_alive == 2:
        pygame.mouse.set_visible(False)
    else:
        pygame.mouse.set_visible(True)


def check_game_hit(ship, aliens, bullets, status, screen_bottom, game_info):
    if (check_hit(ship, aliens) or check_aliens_bottom(aliens, screen_bottom)) and status.game_alive == 2:
        status.ship_limit -= 1
        game_info.ship_list_pop()
        if status.ship_limit > 0:
            reset_status(ship, aliens, bullets, status)
            status.game_alive = 2
        else:
            status.game_alive = 3
        time.sleep(0.5)


def check_hit(ship, aliens):
    if pygame.sprite.spritecollideany(ship, aliens):
        return True
    return False


def check_button_click(mouse_x, mouse_y, button_rect):
    if button_rect.collidepoint(mouse_x, mouse_y):
        return True
    return False


def reset_status(ship, aliens, bullets, status):
    if status.game_alive == 2:
        bullets.empty()
        aliens.empty()
        ship.reset_xy()


def check_aliens_bottom(aliens, screen_bottom):
    for alien in aliens.copy():
        if alien.y > screen_bottom - alien.rect.height:
            return True
    return False


def destroy_bullets(bullets):
    for bullet in bullets.copy():
        if bullet.y < 0:
            bullets.remove(bullet)


def play_button_click(status, settings, game_info, ship, aliens, bullets):
    if status.game_alive == 1 or status.game_alive == 3:
        status.game_alive = 2
        status.ship_limit = settings.ship_limit
        settings.init_dynamic_settings()
        status.score = 0
        game_info.prep_score()
        game_info.prep_ships_left()
        reset_status(ship, aliens, bullets, status)
