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
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """listen to keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        print(event.key)
        if event.key == pygame.K_RIGHT:
            '''move ship to right'''
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            '''move ship to left'''
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        print(event.key)
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
            print("stop")
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
            print("stop")

    def _update_screen(self):
        """draw screen in loop"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        '''make drawn screen visible'''
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
