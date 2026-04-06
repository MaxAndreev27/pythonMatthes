class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.is_fullscreen = False
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 3
        self.ship_limit = 3
        # Параметры снаряда
        self.bullet_speed = 6.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 6
        # Настройки пришельцев
        self.alien_speed = 1.0
        self.fleet_drop_speed = 20
        # fleet_direction = 1 обозначает движение вправо; а -1 — влево.
        self.fleet_direction = 1
