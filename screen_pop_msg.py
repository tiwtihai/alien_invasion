import pygame


class ScreenPopMsg:
    def __init__(self, screen, msg='游戏运行中'):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.msg = msg

        self.msg_size = 60
        self.msg_font = 'SimHei'
        self.msg_color = (30, 144, 255)
        self.msg_obj = pygame.font.SysFont(self.msg_font, self.msg_size)
        self.update_msg(msg)

    def update_msg(self, msg):
        self.msg = msg
        self.msg_surface = self.msg_obj.render(self.msg, True, self.msg_color)

        self.rect = self.msg_surface.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery / 2

    def show_screen_msg(self):
        self.screen.blit(self.msg_surface, self.rect)
