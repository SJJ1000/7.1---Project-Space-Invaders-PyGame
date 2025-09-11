import pygame.font
from pygame.sprite import Group
# from ship import Ship  # will be used when drawing lives

class Scoreboard:
    """Report scoring information (INCOMPLETE)."""

    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # TODO: prepare score/high score/level/ships images
        self.score_image = None
        self.high_score_image = None
        self.level_image = None
        # self.ships = Group()

    def show_score(self):
        """Draw scoreboard elements (TODO)."""
        # TODO: blit prepared images; draw ship icons
        pass
