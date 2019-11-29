class GameStatus:
    def __init__(self, settings):
        self.game_alive = False
        self.ship_limit = settings.ship_limit
        self.game_over=False

