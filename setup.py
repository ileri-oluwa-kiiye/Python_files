import sys

import pygame
from settings import Settings

class AlienInvasion:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialize the game and create game resourses"""
        pygame.init()
        self.settings= Settings()

        self.screen= pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        #Set the background color.
        self.bg_color= (230 , 200, 130)
    
    def run_game(self):
        """Start the main loop for the game"""
        while True:
            #Watch for keyboard and mouse effects
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)

if __name__ == '__main__':
    #Make a game instance and run the game.
    ai= AlienInvasion()
    ai.run_game()