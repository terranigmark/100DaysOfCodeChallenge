# -*- coding: utf-8 -*-
import random

def run():
    elements = ['rock', 'paper', 'scissors']
    random_index = random.randrange(3)
    computer_choice = elements[random_index]

    print('### ROCK-PAPER-SCISSORS ###\n')
    player_choice = str(raw_input('Choose your option to fight the CPU!: '))
    
    while player_choice.lower() != 'rock' and player_choice.lower() != 'paper' and player_choice.lower() != 'scissors':
        print('\nINVALID INPUT! TRY AGAIN')
        player_choice = str(raw_input('Choose your option to fight the CPU!: '))
    else:
        if player_choice.lower() == computer_choice:
            print('ITS A DRAW!')
        elif player_choice.lower() == 'rock' and computer_choice == 'scissors':
            print('YOU WON!')
        elif player_choice.lower() == 'rock' and computer_choice == 'paper':
            print('YOU LOST!')
        elif player_choice.lower() == 'paper' and computer_choice == 'rock':
            print('YOU WON!')
        elif player_choice.lower() == 'paper' and computer_choice == 'scissors':
            print('YOU LOST!')
        elif player_choice.lower() == 'scissors' and computer_choice == 'rock':
            print('YOU LOST!')
        elif player_choice.lower() == 'scissors' and computer_choice == 'paper':
            print('YOU WON!')

    print('Computer choosed: {}'.format(computer_choice))

    

if __name__ == '__main__':
    run()