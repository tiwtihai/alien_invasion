class Settings:
    def __init__(self):
        # 设置屏幕参数
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.screen_top = 50  # 起始坐标
        self.screen_left = 200

        # 飞船移动速度
        self.ship_speed_factor = 1

        # statusbar设置
        self.statusbar_text_color = (30, 144, 255)
        self.statusbar_text_font = 'SimHei'
        self.statusbar_text_size = 16
        self.statusbar_starxy = (0, 0)

        # 设置子弹
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_factor = 1
        self.bullet_color = 60, 60, 60

        # 设置外星人有关参数
        self.alien_factor=1
