class Settings:
    """Store settings (INCOMPLETE)."""

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
        self.bullets_allowed = 3

        # Aliens
        self.fleet_drop_speed = 10

        # Speed scaling (to be used later)
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        # TODO: initialize dynamic speeds and scoring
        # self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Init speeds and scoring (TODO)."""
        # TODO: set ship_speed, bullet_speed, alien_speed, fleet_direction, alien_points
        raise NotImplementedError("initialize_dynamic_settings() pending")

    def increase_speed(self):
        """Scale up speeds and points (TODO)."""
        raise NotImplementedError("increase_speed() pending")
