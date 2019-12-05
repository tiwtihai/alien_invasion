import pygame


class Buttons:
    def __init__(self, screen):
        self.screen = screen

        self.button_width, self.button_height = 180, 40
        self.button_color = (255, 153, 0)

        self.frame_color = (255, 102, 0)
        self.frame_width = self.button_width + 5
        self.frame_height = self.button_height + 5

        self.text_font = 'SimHei'
        self.text_size = 26
        self.text_color = (30, 144, 255)

        # play_button
        self.play_button_rect = pygame.Rect(0, 0, self.button_width, self.button_height)
        self.play_frame_rect = pygame.Rect(0, 0, self.frame_width, self.frame_height)
        self.play_button_text = '开始游戏(S)'
        self.play_button_text_obj = pygame.font.SysFont(self.text_font, self.text_size)
        self.play_button_text_surface = self.play_button_text_obj.render(self.play_button_text, True, self.text_color)
        self.play_button_text_rect = self.play_button_text_surface.get_rect()

        self.play_button_text_rect.center = self.screen.get_rect().center
        self.play_button_rect.center = self.play_button_text_rect.center
        self.play_frame_rect.center = self.play_button_text_rect.center

        # quit_button
        self.quit_button_rect = pygame.Rect(0, 0, self.button_width, self.button_height)
        self.quit_frame_rect = pygame.Rect(0, 0, self.frame_width, self.frame_height)
        self.quit_button_text = '退出游戏(Q)'
        self.quit_button_text_obj = pygame.font.SysFont(self.text_font, self.text_size)
        self.quit_button_text_surface = self.quit_button_text_obj.render(self.quit_button_text, True, self.text_color)
        self.quit_button_text_rect = self.quit_button_text_surface.get_rect()

        self.quit_button_text_rect.center = self.play_button_text_rect.centerx, self.play_button_text_rect.centery + 80
        self.quit_button_rect.center = self.quit_button_text_rect.center
        self.quit_frame_rect.center = self.quit_button_text_rect.center

    def show_play_button(self):
        self.screen.fill(self.frame_color, self.play_frame_rect)
        self.screen.fill(self.button_color, self.play_button_rect)
        self.screen.blit(self.play_button_text_surface, self.play_button_text_rect)

    def show_quit_button(self):
        self.screen.fill(self.frame_color, self.quit_frame_rect)
        self.screen.fill(self.button_color, self.quit_button_rect)
        self.screen.blit(self.quit_button_text_surface, self.quit_button_text_rect)
