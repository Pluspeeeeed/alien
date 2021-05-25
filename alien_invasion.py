import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):
        """main loop"""
        while True:
            '''listen for keyboard and mouse'''
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            '''draw screen in loop'''
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            '''make drawn screen visible'''
            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
