import pygame

class Button:
    """Simple centered button (INCOMPLETE)."""

    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # TODO: render msg to image
        self.msg_image = None
        self.msg_image_rect = None

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        # TODO: blit text when prepared
        # self.screen.blit(self.msg_image, self.msg_image_rect)
