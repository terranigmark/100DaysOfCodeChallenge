# -*- coding: utf-8 -*-
import random

def run():
    #Generating random value to guess
    random_number = random.randrange(1001)
    tries = 0
    guess = 0

    print('### GUESS GAME ###')

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

if __name__ == '__main__':
    run()