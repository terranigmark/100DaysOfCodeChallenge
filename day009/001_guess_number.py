# -*- coding: utf-8 -*-
import random
    
def run():
    #Generating random value to guess
    tries = 0
    guess = 0
    game = True
    option = 'y'

    print('### GUESS GAME ###')

    while game == True:
        random_number = random.randrange(4)

        while guess != random_number:
            print('\nGuess the secret number from 0 to 1000')
            guess = int(raw_input('Enter your guess: '))

            if guess < random_number:
                print('WRONG NUMBER! Try with a HIGHER number')
                tries += 1
            elif guess > random_number:
                print('WRONG NUMBER! Try with a LOWER number')
                tries += 1
            else:
                print('\nYOU WON! The secret number was {}'.format(random_number))
                print('It only took you {} tries'.format(tries))

                tries = 0
        
        option = str(raw_input('\nPlay again? [Y/N]: '))

        if option.lower() == 'y':
            game = True
        else:
            game = False

    else:
        print('\n****G A M E  O V E R****')

if __name__ == '__main__':
    run()