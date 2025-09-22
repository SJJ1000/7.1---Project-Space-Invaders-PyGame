class Settings:
    """Store all settings for Alien Invasion."""

    def __init__(self):
        # Screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship
        self.ship_limit = 3

        # Bullets
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3  # book’s setting

        # Aliens
        self.fleet_drop_speed = 10

        # Speed scaling (Ch. 14)
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = .3

        # 1 = right, -1 = left
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= (self.speedup_scale * 0.5)
        self.fleet_drop_speed *= 1.02
        self.alien_points = int(self.alien_points * self.score_scale)

