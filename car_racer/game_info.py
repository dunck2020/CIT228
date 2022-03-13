import time

class GameInfo:
    '''basic level information'''
    levels = 10
    def __init__ (self, level=1):
        self.level = level
        self.started = False
        self.level_start_time = 0
    '''increment level when player wins'''
    def next_level(self):
        self.level += 1
        self.started = False
    '''reset levels when player loses'''
    def reset(self):
        self.level = 1
        self.started = False
        self.level_start_time = 0
    '''notify ai player wins'''
    def game_finished(self):
        return self.level > self.levels
    '''function to determine if game has started'''
    def start_level(self):
        self.started = True
        self.level_start_time = time.time()
    '''timer for level'''
    def get_level_time(self):
        if not self.started:
            return 0
        return round(time.time() - self.level_start_time)

