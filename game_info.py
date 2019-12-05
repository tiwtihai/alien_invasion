import pygame


class GameInfo:
    def __init__(self, screen, ship, settings, bullets_num, aliens_num, status):

        self.screen = screen
        self.ship = ship
        self.status = status
        self.settings = settings
        self.screen_rect = screen.get_rect()

        # 初始化状态栏status_bar参数
        self.statusbar_text_font = settings.statusbar_text_font
        self.statusbar_text_size = settings.statusbar_text_size
        self.statusbar_text_color = settings.statusbar_text_color
        self.statusbar_starxy = settings.statusbar_starxy
        self.statusbar_contents = '飞船[x:%d, y:%d] | 子弹数量:%d | 外星生物数量:%d'
        self.statusbar_img_obj = pygame.font.SysFont(self.statusbar_text_font, self.statusbar_text_size)
        self.prep_statusbar(bullets_num, aliens_num)

        # 初始化socre_board参数
        self.score_color = (30, 30, 30)
        self.score_font = pygame.font.SysFont(None, 40)
        self.prep_score()

        # 初始化hight_score
        self.high_score_color = (30, 30, 30)
        self.high_score_font = pygame.font.SysFont('SimHei', 20)
        self.prep_high_score()

        # 初始化显示飞船生命个数
        self.ship_list = []
        self.ship_img_width = int(self.ship.image.get_size()[0]*0.6)
        self.ship_img_height = int(self.ship.image.get_size()[1]*0.6)
        self.ship_img=pygame.image.load('./images/ship.png')
        self.ship_img=pygame.transform.scale(self.ship_img, (self.ship_img_width, self.ship_img_height))

        # self.prep_ships_left()

    def prep_ships_left(self):
        for ship_left in range(self.status.ship_limit):
            new_ship = self.ship_img
            ship_rect = new_ship.get_rect()
            ship_rect.bottom = self.screen_rect.height - 10
            ship_rect.right = self.screen_rect.width-10 - ship_left*ship_rect.width
            self.ship_list.append((new_ship, ship_rect))
    
    def ship_list_pop(self):
        if len(self.ship_list)>0:
            self.ship_list.pop()

    def prep_high_score(self):
        rounded_high_score = round(self.status.high_score, -1)
        high_score_str = '{:,}'.format(rounded_high_score)
        high_score_str = '最高：'+high_score_str
        self.high_score_img = self.high_score_font.render(high_score_str, True, self.high_score_color)
        self.high_score_rect = self.high_score_img.get_rect()
        self.high_score_rect.right = self.settings.screen_width-10
        self.high_score_rect.top = 10

    def prep_score(self):
        rounded_score = round(self.status.score, -1)
        score_str = '{:,}'.format(rounded_score)
        self.score_img = self.score_font.render(score_str, True, self.score_color)
        self.score_rect = self.score_img.get_rect()
        self.score_rect.top = 20
        self.score_rect.centerx = self.screen_rect.centerx

    def prep_statusbar(self, bullets_num, aliens_num):
        self.statusbar_surface = self.statusbar_img_obj.render(
            self.statusbar_contents % (
                self.ship.centerx, self.ship.centery, bullets_num, aliens_num), True,
            self.statusbar_text_color)
        self.statusbar_rect = self.statusbar_surface.get_rect()
        self.statusbar_rect.topleft = self.statusbar_starxy

    def show_game_info(self):
        self.screen.blit(self.statusbar_surface, self.statusbar_rect)
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_img, self.high_score_rect)
        for ship_num in range(len(self.ship_list)):
            self.screen.blit(self.ship_list[ship_num][0], self.ship_list[ship_num][1])
