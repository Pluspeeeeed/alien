import sys

import pygame


class AlienInvasion:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        '''set bg color'''
        self.bg_color = 230, 230, 230


    def run_game(self):
        '''Main loop'''
        while True:
            '''listen for keyboard and mouse'''
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            '''draw bg color'''
            self.screen.fill(self.bg_color)

            '''make drawn screen visible'''
            pygame.display.flip()



if __name__ == '__main__'
    ai = AlienInvasion()
    ai.run_game()