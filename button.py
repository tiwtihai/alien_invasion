import pygame


class Button:
    def __init__(self, screen, text):
        self.screen = screen

        self.button_width, self.button_height = 180, 40
        self.button_color = (255,153,0)
        self.button_rect = pygame.Rect(0, 0, self.button_width, self.button_height)

        self.frame_color = (255,102,0)
        # self.frame_color = (0, 255, 0)
        self.frame_width = self.button_width + 5
        self.frame_height = self.button_height + 5
        self.frame_rect = pygame.Rect(0, 0, self.frame_width, self.frame_height)

        self.text = text
        self.text_font = 'SimHei'
        self.text_size = 26
        self.text_color = (30, 144, 255)
        self.text_font_obj = pygame.font.SysFont(self.text_font, self.text_size)
        self.text_surface = self.text_font_obj.render(self.text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect()

        self.button_rect.center = self.screen.get_rect().center
        self.text_rect.center = self.button_rect.center
        self.frame_rect.center = self.button_rect.center

    def show_button(self):
        self.screen.fill(self.frame_color, self.frame_rect)
        self.screen.fill(self.button_color, self.button_rect)
        self.screen.blit(self.text_surface, self.text_rect)
