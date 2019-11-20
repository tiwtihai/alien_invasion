import pygame


class StatusBar:
    def __init__(self, screen, ship_x, ship_y, game_settings, bullets_num):
        self.screen = screen
        self.text_font_obj = pygame.font.SysFont(game_settings.statusbar_text_font, game_settings.statusbar_text_size)
        self.text_surface = self.text_font_obj.render('x:%d, y:%d | bullets:%d' % (ship_x, ship_y, bullets_num), True,
                                                      game_settings.statusbar_text_color)
        self.text_rect = self.text_surface.get_rect()

    def update(self, ship_x, ship_y, game_settings, bullets_num):
        self.text_surface = self.text_font_obj.render('x:%d, y:%d | bullets:%d' % (ship_x, ship_y, bullets_num), True,
                                                      game_settings.statusbar_text_color)
        self.text_rect.topleft = game_settings.statusbar_starxy

    def print_text(self):
        self.screen.blit(self.text_surface, self.text_rect)
