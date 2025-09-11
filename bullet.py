import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Bullets fired from the ship (INCOMPLETE)."""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # TODO: align to ship midtop when ship is implemented
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.center = (self.settings.screen_width // 2, self.settings.screen_height // 2)

        self.y = float(self.rect.y)

    def update(self):
        """Move bullet upward (TODO: use bullet_speed)."""
        # TODO: self.y -= self.settings.bullet_speed
        pass

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
