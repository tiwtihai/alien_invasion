class GameStatus:
    def __init__(self, settings):
        # 游戏准备状态:game_alive = 1
        # 正在玩游戏状态：game_alive = 2
        # game_over:game_alive = 3
        # 暂停game_alive = 4
        self.game_alive = 1
        self.ship_limit = settings.ship_limit

        self.score = 0
        self.high_score = 0

        self.level = 1
        self.high_level = 1
        self.filename = settings.record_file
        self.read_record()

    def save_record(self):
        self.record = 'high_level=' + str(self.high_level) + '\n' + 'high_score=' + str(self.high_score)
        try:
            with open(self.filename, 'w') as f_obj:
                f_obj.write(self.record)
        except:
            pass

    def read_record(self):
        try:
            with open(self.filename) as f_obj:
                for line in f_obj.readlines():
                    line_record = line.split('=')
                    if line_record[0] == 'high_level':
                        self.high_level = int(line_record[1])
                    if line_record[0] == 'high_score':
                        self.high_score = int(line_record[1])
        except:
            pass
