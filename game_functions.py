import sys
import pygame
from bullet import Bullet
from alien import Alien


def check_events(screen, ship, settings, bullets):
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


def update_screen(settings, screen, ship, statusbar, bullets, aliens):
    screen.fill(settings.bg_color)
    for alien in aliens.sprites():
        alien.blitme()
    ship.blitme()
    statusbar.print_text()
    for bullet in bullets.sprites():
        bullet.launch()
    pygame.display.flip()


def creat_aliens(aliens, screen, settings):
    alien_model = Alien(screen, settings)
    alien_width = alien_model.rect.width
    alien_height = alien_model.rect.height
    screen_width = settings.screen_width
    # screen_height = settings.screen_height

    aliens_rows = settings.aliens_rows
    aliens_rows_max = int(screen_width / alien_width)
    if aliens_rows > aliens_rows_max:
        aliens_rows = aliens_rows_max
    aliens_space_x = (screen_width - alien_width * aliens_rows) / (aliens_rows + 1)

    aliens_lines = settings.aliens_lines
    aliens_space_y = alien_height / 2

    for line in range(1, aliens_lines + 1):
        for row in range(1, aliens_rows + 1):
            alien = Alien(screen, settings)
            alien.rect.x = aliens_space_x * row + alien_width * (row - 1)
            alien.rect.y = -(aliens_space_y * (line - 1) + alien_height * line) + alien_height
            aliens.add(alien)


def check_edge(aliens, screen_width):
    for alien in aliens.sprites():
        # print('%s:x->%d,y->%d' % (str(id(alien)), alien.rect.x, alien.rect.y))
        if alien.rect.right >= screen_width or alien.rect.left <= 0:
            return True
    return False


def update_bullets(bullets):
    bullets.update()
    destroy_bullets(bullets)


def update_aliens(aliens, screen_width, screen_bottom):
    aliens.update(check_edge(aliens, screen_width))
    destroy_aliens(aliens, screen_bottom)


def check_fire(bullets, aliens, screen, settings):
    pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        bullets.empty()
        creat_aliens(aliens, screen, settings)


def check_game_over():
    pass


def check_hit(ship, aliens):
    if pygame.sprite.spritecollide(ship, aliens):
        return True


def destroy_bullets(bullets):
    for bullet in bullets.copy():
        if bullet.y < 0:
            bullets.remove(bullet)


def destroy_aliens(aliens, scree_bottom):
    for alien in aliens.copy():
        if alien.y > scree_bottom:
            aliens.remove(alien)
