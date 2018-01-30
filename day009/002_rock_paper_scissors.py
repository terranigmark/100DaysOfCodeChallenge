# -*- coding: utf-8 -*-
import random

def run():
    game = True
    elements = ['rock', 'paper', 'scissors']
    random_index = random.randrange(3)

    print('### ROCK-PAPER-SCISSORS ###\n')
    player_choice = str(raw_input('Choose your option to fight the CPU!: '))
    
    while game == True:

        computer_choice = elements[random_index]

        while player_choice.lower() != 'rock' and player_choice.lower() != 'paper' and player_choice.lower() != 'scissors':
            print('\nINVALID INPUT! TRY AGAIN')
            player_choice = str(raw_input('Choose your option to fight the CPU!: '))
        else:
            if player_choice.lower() == computer_choice:
                print('ITS A DRAW!')
                print('Computer choosed: {}'.format(computer_choice))
            elif player_choice.lower() == 'rock' and computer_choice == 'scissors':
                print('YOU WON!')
                print('Computer choosed: {}'.format(computer_choice))
            elif player_choice.lower() == 'rock' and computer_choice == 'paper':
                print('YOU LOST!')
                print('Computer choosed: {}'.format(computer_choice))
            elif player_choice.lower() == 'paper' and computer_choice == 'rock':
                print('YOU WON!')
                print('Computer choosed: {}'.format(computer_choice))
            elif player_choice.lower() == 'paper' and computer_choice == 'scissors':
                print('YOU LOST!')
                print('Computer choosed: {}'.format(computer_choice))
            elif player_choice.lower() == 'scissors' and computer_choice == 'rock':
                print('YOU LOST!')
                print('Computer choosed: {}'.format(computer_choice))
            elif player_choice.lower() == 'scissors' and computer_choice == 'paper':
                print('YOU WON!')
                print('Computer choosed: {}'.format(computer_choice))
        
        option = str(raw_input('\nPlay again? [Y/N]: '))

        if option.lower() == 'y':
            game = True
        elif option.lower() == 'n':
            game = False
        else:
            print('INVALD OPTION')
            option = str(raw_input('Play again? [Y/N]: '))

    else:
        print('\n****G A M E  O V E R****')

if __name__ == '__main__':
    run()