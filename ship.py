import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Manage the player's ship (INCOMPLETE)."""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # TODO: load image later and compute rect
        # self.image = pygame.image.load("ship.bmp")
        # self.rect = self.image.get_rect()

        # Placeholder rect so file imports; will replace with image rect later
        self.rect = pygame.Rect(0, 0, 60, 48)
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update ship position (TODO: respect image width & speeds)."""
        # TODO: use self.settings.ship_speed when dynamic settings exist
        pass

    def blitme(self):
        """Draw ship (TODO: blit actual image)."""
        # self.screen.blit(self.image, self.rect)
        pygame.draw.rect(self.screen, (0, 0, 255), self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
