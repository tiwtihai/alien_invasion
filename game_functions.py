import sys
import pygame
from bullet import Bullet
from alien import Alien
import time


def check_events(screen, ship, settings, bullets, play_button, gamestatus):
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
                new_bullet = Bullet(screen, ship, settings)
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

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if check_play_button(mouse_x, mouse_y, play_button.button_rect):
                gamestatus.game_alive = True
                if gamestatus.game_over:
                    sys.exit()


def update_screen(settings, screen, ship, statusbar, bullets, aliens, play_button, replay_button, gamestatus):
    screen.fill(settings.bg_color)
    for alien in aliens.sprites():
        alien.blitme()
    statusbar.print_text()
    for bullet in bullets.sprites():
        bullet.launch()
    ship.blitme()
    if gamestatus.game_alive is False:
        play_button.show_button()
    if gamestatus.game_over:
        replay_button.show_button()
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
    destroy_aliens(aliens, settings.screen_height)
    if len(aliens) == 0 and game_alive:
        bullets.empty()
        creat_aliens(aliens, screen, settings)


def check_fire(bullets, aliens):
    if pygame.sprite.groupcollide(bullets, aliens, True, True):
        return True
    return False


def check_game_over(status):
    if status.ship_limit > 0:
        status.game_alive = True
    else:
        status.game_alive = False
        status.game_over = True


def check_game_status(ship, aliens, bullets, status, screen_bottom):
    if (check_hit(ship, aliens) or check_aliens_bottom(aliens, screen_bottom)) and status.game_alive:
        status.ship_limit -= 1
        if status.ship_limit > 0:
            reset_status(ship, aliens, bullets, status)
        time.sleep(0.5)


def check_hit(ship, aliens):
    if pygame.sprite.spritecollideany(ship, aliens):
        return True
    return False


def check_play_button(mouse_x, mouse_y, button_rect):
    if button_rect.collidepoint(mouse_x, mouse_y):
        return True
    return False


def reset_status(ship, aliens, bullets, status):
    if status.game_alive is True:
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


def destroy_aliens(aliens, screen_bottom):
    for alien in aliens.copy():
        if alien.y > screen_bottom:
            aliens.remove(alien)


def set_btn_pos(button, pos):
    button.button_rect.center = pos[0], pos[1] + 80
    button.text_rect.center = button.button_rect.center
    button.frame_rect.center = button.button_rect.center
