class Settings:
    """A class to store all the settings for the Alien Invasion game"""
    def __init__(self):
        """Initialize the game's static settings"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_limit = 2

        # bullet settings
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # alien settings
        self.fleet_drop_speed = 10

        # how quickly the game speeds up
        self.speed_up_scale = 1.1

        # how quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1

        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1 

        # scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien points value"""
        self.ship_speed *= self.speed_up_scale
        self.bullet_speed *= self.speed_up_scale
        self.alien_speed *= self.speed_up_scale

        self.alien_points = int(self.alien_points * self.score_scale)

