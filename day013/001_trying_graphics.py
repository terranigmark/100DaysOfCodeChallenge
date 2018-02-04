# -*- coding: utf-8 -*-

def run():
    # Import a library of functions called 'pygame'
    import pygame
    # Initialize the game engine
    pygame.init()

    # Define some colors
    BLACK   = (   0,  0,  0)
    WHITE   = ( 255, 255, 255)
    GREEN   = ( 0, 255, 0)
    RED     = (255, 0,  0)

    # Generate a window
    size = (700, 500)
    screen = pygame.display.set_mode(size)
    screen.fill(WHITE)

    # Adding a title to the window
    pygame.display.set_caption('THIS IS A MOTHER F-ING GAME!')

    # Loop until the user clicks the close button
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # ------ Main Program Loop ------
    while not done:
        # --- Main event loop
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                print('User asked to quit.')
                done = True # Flag that we are done so we exit this loop
            elif event.type == pygame.KEYDOWN:
                print('User pressed a key.')
            elif event.type == pygame.KEYUP:
                print('User let go of a key.')
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print('User pressed a mouse button')
        
        #pygame.draw.rect(screen, GREEN, [50, 50, 100, 100])
        

    # --- Game logic should go here

    # --- Drawing code should go here

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command

    # --- Go ahead and update the screen with what we've drawn

    # --- Limit to 60 frames per second
    clock.tick(60)

if __name__ == '__main__':
    run()