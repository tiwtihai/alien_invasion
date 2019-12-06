class Settings:
    def __init__(self):
        # 设置屏幕参数
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.screen_top = 50  # 起始坐标
        self.screen_left = 200

        self.ship_limit = 3

        # statusbar设置
        self.statusbar_text_color = (30, 144, 255)
        self.statusbar_text_font = 'SimHei'
        self.statusbar_text_size = 16
        self.statusbar_starxy = (10, self.screen_height - self.statusbar_text_size - 10)

        # 设置子弹
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60

        # 设置外星人有关参数
        self.aliens_rows = 7
        self.aliens_lines = 4
        self.alien_drop_interval = 20

        self.record_file = 'record.txt'

        self.init_dynamic_settings()

    def init_dynamic_settings(self):
        # 飞船移动速度
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 1
        self.aliens_move_lr = 1  # 1往右移动，-1往左移动
        self.lv_increase_factor = 1.5
        # 记分
        self.alien_point = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.lv_increase_factor
        self.bullet_speed_factor *= self.lv_increase_factor
        self.alien_speed_factor *= self.lv_increase_factor
        self.alien_drop_interval *= self.lv_increase_factor
        self.alien_point *= self.lv_increase_factor
