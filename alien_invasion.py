import sys
import pygame

from settings import Settings
# from ship import Ship
# from bullet import Bullet
# from alien import Alien
# from game_stats import GameStats
# from button import Button
# from scoreboard import Scoreboard


class AlienInvasion:
    """Overall class to manage game assets and behavior (INCOMPLETE)."""

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        # Basic window; will adjust later
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion (WIP)")

        # TODO: initialize Ship, Groups, Stats, Scoreboard, Play button
        # self.ship = Ship(self)
        # self.bullets = pygame.sprite.Group()
        # self.aliens = pygame.sprite.Group()
        # self.stats = GameStats(self)
        # self.sb = Scoreboard(self)
        # self.play_button = Button(self, "Play")

        # TODO: create initial fleet
        # self._create_fleet()

    def run_game(self):
        """Main loop (bare minimum)."""
        while True:
            self._check_events()
            # TODO: update ship, bullets, aliens when game_active
            # if self.stats.game_active:
            #     self.ship.update()
            #     self._update_bullets()
            #     self._update_aliens()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # TODO: handle KEYDOWN/KEYUP and MOUSEBUTTONDOWN
            # elif event.type == pygame.KEYDOWN:
            #     self._check_keydown_events(event)
            # elif event.type == pygame.KEYUP:
            #     self._check_keyup_events(event)
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     mouse_pos = pygame.mouse.get_pos()
            #     self._check_play_button(mouse_pos)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        # TODO: draw bullets, ship, aliens, scoreboard, and play button when inactive
        pygame.display.flip()

    # TODO: below helpers will be implemented in later commits
    # def _check_keydown_events(self, event): ...
    # def _check_keyup_events(self, event): ...
    # def _check_play_button(self, mouse_pos): ...
    # def _fire_bullet(self): ...
    # def _update_bullets(self): ...
    # def _check_bullet_alien_collisions(self): ...
    # def _create_fleet(self): ...
    # def _create_alien(self, alien_number, row_number): ...
    # def _update_aliens(self): ...
    # def _check_fleet_edges(self): ...
    # def _change_fleet_direction(self): ...
    # def _ship_hit(self): ...
    # def _check_aliens_bottom(self): ...


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
