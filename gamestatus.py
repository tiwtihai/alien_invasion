class GameStatus:
    def __init__(self, settings):
        
        # 游戏准备状态:game_alive = 1
        # 正在玩游戏状态：game_alive = 2
        # game_over:game_alive = 3
        self.game_alive = 1
        self.ship_limit = settings.ship_limit
