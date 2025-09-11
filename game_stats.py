class GameStats:
    """Track statistics (INCOMPLETE)."""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.game_active = False
        self.high_score = 0
        self.reset_stats()  # TODO: implement properly

    def reset_stats(self):
        """Stats that change during the game (TODO)."""
        # TODO: set ships_left, score, level
        pass
