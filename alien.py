import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A single alien (INCOMPLETE)."""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # TODO: load image later
        # self.image = pygame.image.load("alien.bmp")
        # self.rect = self.image.get_rect()

        self.rect = pygame.Rect(0, 0, 50, 40)  # placeholder
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien at edge (TODO)."""
        # TODO: use screen rect and real image width
        return False

    def update(self):
        """Move alien (TODO: use alien_speed and fleet_direction)."""
        pass
