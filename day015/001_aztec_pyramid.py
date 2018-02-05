# -*- coding: utf-8 -*-

import pygame
import math

def run():
    # Define some variables
    y_origin_offset = -30
    x_origin_offset = 35
    y_drawing_offset = 0
    x_drawing_offset = 0
    
    # Define some colors & constants
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    DARK_GRAY = (104, 104, 104)
    GRAY = (168, 168, 168)
    LIGHT_GRAY = (209, 209, 209)
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

        # Drawing steps
        for steps in range(1, 315, 35):
            pygame.draw.rect(screen, BLACK, [50 + (steps/1.45), 450 - steps, 600 - (steps*1.35), 36], 3)
            for length in range(1, 600, 20):
                pygame.draw.line(screen, BLACK, [50 + length, 470], [60 + length, 470], 1)
                pygame.draw.line(screen, BLACK, [60 + length, 470], [60 + length, 460], 1)
                pygame.draw.line(screen, BLACK, [60 + length, 460], [70 + length, 460], 1)
                pygame.draw.line(screen, BLACK, [70 + length, 460], [70 + length, 470], 1)
                




        # Drawing stairs & its borders
        pygame.draw.polygon(screen, LIGHT_GRAY, ([250, 484], [260, 484], [320, 168], [310, 168]))
        pygame.draw.polygon(screen, LIGHT_GRAY, ([450, 484], [440, 484], [390, 168], [400, 168]))
        pygame.draw.polygon(screen, BLACK, ([250, 484], [260, 484], [320, 168], [310, 168]), 3)
        pygame.draw.polygon(screen, BLACK, ([450, 484], [440, 484], [390, 168], [400, 168]), 3)

        #-- Drawing top chamber
        #- Structure
        pygame.draw.rect(screen, DARK_GRAY, [263, 94, 180, 75])
        pygame.draw.rect(screen, BLACK, [263, 94, 180, 75], 2)
        
        #- Details
        # Lines in top chamber
        pygame.draw.rect(screen, GRAY, [263, 114, 180, 7])
        pygame.draw.rect(screen, BLACK, [263, 114, 180, 7], 1)
        pygame.draw.rect(screen, GRAY, [263, 135, 180, 7])
        pygame.draw.rect(screen, BLACK, [263, 135, 180, 7], 1)
        
        #  Windows in top chamber - LEFT
        pygame.draw.rect(screen, BLACK, [275, 100, 14, 14])
        pygame.draw.line(screen, GRAY, [275, 114], [275,100], 1)
        pygame.draw.line(screen, GRAY, [275, 100], [289,100], 1)
        pygame.draw.line(screen, GRAY, [289, 100], [289,114], 1)

        #  Windows in top chamber - RIGHT
        pygame.draw.rect(screen, BLACK, [419, 100, 14, 14])
        pygame.draw.line(screen, GRAY, [419, 114], [419,100], 1)
        pygame.draw.line(screen, GRAY, [419, 100], [433,100], 1)
        pygame.draw.line(screen, GRAY, [433, 100], [433,114], 1)

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