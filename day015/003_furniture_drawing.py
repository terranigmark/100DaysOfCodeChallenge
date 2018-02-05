# -*- coding: utf-8 -*-
import pygame
import math

def run():
    # General constants
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    PI = 3.141592653

    # General variables
    steps_x_offset_origin = 0
    STEPS_Y_OFFSET_ORIGIN = 0
    steps_y_offset_draw = 0
    steps_x_offset_draw = 0

    # Initializing library
    pygame.init()

    # Set the width and height of the screen [width, height]
    size = (900, 700)
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
        
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command
        screen.fill(WHITE)

        # --- Drawing code should go here
        # Drawing the main structure
        for steps in range(1, 10):
            pygame.draw.rect(screen, BLACK, [100 + steps_x_offset_origin, 600 - STEPS_Y_OFFSET_ORIGIN, 700 - steps_x_offset_draw, 50], 3)
            steps_x_offset_origin += 3
            STEPS_Y_OFFSET_ORIGIN += 5
            steps_x_offset_draw += 3

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()


if __name__ == '__main__':
    run()