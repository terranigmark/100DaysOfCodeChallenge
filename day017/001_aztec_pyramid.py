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
    SKY_BLUE = (77, 190, 242)
    GREEN = (14, 234, 36)
    YELLOW = (255, 250, 0)
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

        # Drawing background
        pygame.draw.rect(screen, SKY_BLUE, [0, 0, 700, 350])
        pygame.draw.rect(screen, GREEN, [0, 350, 700, 500])
        pygame.draw.circle(screen, YELLOW, (420, 50), 20, 0)
        

        # Drawing steps
        for steps in range(1, 315, 35):
            pygame.draw.rect(screen, GRAY, [50 + (steps/1.45), 450 - steps, 600 - (steps*1.35), 36], 0)
            pygame.draw.rect(screen, BLACK, [50 + (steps/1.45), 450 - steps, 600 - (steps*1.35), 36], 3)
        # Fisrt step decorations
        for length in range(1, 600, 20):
            pygame.draw.line(screen, BLACK, [50 + length, 470], [60 + length, 470], 1)
            pygame.draw.line(screen, BLACK, [60 + length, 470], [60 + length, 460], 1)
            pygame.draw.line(screen, BLACK, [60 + length, 460], [70 + length, 460], 1)
            pygame.draw.line(screen, BLACK, [70 + length, 460], [70 + length, 470], 1)
        # Second step decorations
        for length in range(1, 540, 20):
            pygame.draw.line(screen, BLACK, [75 + length, 434], [85 + length, 434], 1)
            pygame.draw.line(screen, BLACK, [85 + length, 434], [85 + length, 426], 1)
            pygame.draw.line(screen, BLACK, [85 + length, 426], [95 + length, 426], 1)
            pygame.draw.line(screen, BLACK, [95 + length, 426], [95 + length, 433], 1)
        # Third step decorations
        for length in range(1, 500, 20):
            pygame.draw.line(screen, BLACK, [97 + length, 398], [107 + length, 398], 1)
            pygame.draw.line(screen, BLACK, [107 + length, 398], [107 + length, 390], 1)
            pygame.draw.line(screen, BLACK, [107 + length, 390], [117 + length, 390], 1)
            pygame.draw.line(screen, BLACK, [117 + length, 390], [117 + length, 398], 1)
        # Fourth step decorations
        for length in range(1, 460, 20):
            pygame.draw.line(screen, BLACK, [123 + length, 362], [133 + length, 362], 1)
            pygame.draw.line(screen, BLACK, [133 + length, 362], [133 + length, 354], 1)
            pygame.draw.line(screen, BLACK, [133 + length, 354], [143 + length, 354], 1)
            pygame.draw.line(screen, BLACK, [143 + length, 354], [143 + length, 362], 1)
        # Fifth step decorations
        for length in range(1, 420, 20):
            pygame.draw.line(screen, BLACK, [145 + length, 326], [155 + length, 326], 1)
            pygame.draw.line(screen, BLACK, [155 + length, 326], [155 + length, 318], 1)
            pygame.draw.line(screen, BLACK, [155 + length, 318], [165 + length, 318], 1)
            pygame.draw.line(screen, BLACK, [165 + length, 318], [165 + length, 326], 1)
        # Sixth step decorations
        for length in range(1, 360, 20):
            pygame.draw.line(screen, BLACK, [170 + length, 290], [180 + length, 290], 1)
            pygame.draw.line(screen, BLACK, [180 + length, 290], [180 + length, 282], 1)
            pygame.draw.line(screen, BLACK, [180 + length, 282], [190 + length, 282], 1)
            pygame.draw.line(screen, BLACK, [190 + length, 282], [190 + length, 290], 1)
        # Seventh step decorations
        for length in range(1, 320, 20):
            pygame.draw.line(screen, BLACK, [193 + length, 254], [203 + length, 254], 1)
            pygame.draw.line(screen, BLACK, [203 + length, 254], [203 + length, 246], 1)
            pygame.draw.line(screen, BLACK, [203 + length, 246], [213 + length, 246], 1)
            pygame.draw.line(screen, BLACK, [213 + length, 246], [213 + length, 254], 1)
        # Eight step decorations
        for length in range(1, 260, 20):
            pygame.draw.line(screen, BLACK, [218 + length, 225], [228 + length, 225], 1)
            pygame.draw.line(screen, BLACK, [228 + length, 225], [228 + length, 217], 1)
            pygame.draw.line(screen, BLACK, [228 + length, 217], [238 + length, 217], 1)
            pygame.draw.line(screen, BLACK, [238 + length, 217], [238 + length, 225], 1)
        # Nineth step decorations
        for length in range(1, 220, 20):
            pygame.draw.line(screen, BLACK, [241 + length, 189], [251 + length, 189], 1)
            pygame.draw.line(screen, BLACK, [251 + length, 189], [251 + length, 181], 1)
            pygame.draw.line(screen, BLACK, [251 + length, 181], [261 + length, 181], 1)
            pygame.draw.line(screen, BLACK, [261 + length, 181], [261 + length, 189], 1)

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

        #  Windows in highest step
        pygame.draw.rect(screen, BLACK, [322, 147, 66, 22])
        for i in range(1, 66, 22):
            pygame.draw.rect(screen, GRAY, [322 + i, 147, 22, 22], 2)
        pygame.draw.line(screen, BLACK, [322, 169], [388, 169], 3)

        
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