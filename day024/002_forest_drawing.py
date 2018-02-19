# -*- coding: utf-8 -*-

import pygame
import math

def draw_tree(screen, size, BROWN, GREEN):
    pygame.draw.rect(screen, BROWN, [60, 400, 30, 45])
    pygame.draw.polygon(screen, GREEN, [[150, 400], [75, 250], [0, 400]])
    pygame.draw.polygon(screen, GREEN, [[140, 350], [75, 230], [10, 350]])


def run():
    # Define some variables
    
    # Define some colors & constants
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    DARK_GRAY = (104, 104, 104)
    GRAY = (168, 168, 168)
    LIGHT_GRAY = (209, 209, 209)
    SKY_BLUE = (77, 190, 242)
    GREEN = (14, 234, 36)
    YELLOW = (255, 250, 0)
    BROWN = (130, 42, 5)
    PI = 3.141592653
    
    pygame.init()

    # Set the width and height of the screen [width, height]
    size = (700, 500)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption('Aztec Pyramid')

    # Loop until the user clicks the close button
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop ---------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # --- Game logic should go here

        # --- Drawing code should go here
        
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command
        screen.fill(WHITE)

        # Drawing 
        draw_tree(screen, size, BROWN, GREEN)

        # --- Update screen's drawing
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()

if __name__ == '__main__':
    run()