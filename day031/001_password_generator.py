# -*- coding: utf-8 -*-
# Importing libraries
from __future__ import print_function
import random

def generate_new_pass(password, password_list, pass_index):
    pass_length = int(raw_input('Choose the character length of your password: ')) #Defines password strength
    for i in range(0, pass_length):
        #print(chr(random.randrange(32,126)), end='')
        password.join(chr(random.randrange(32,126)))
        
    print(password)
    password_list.extend(password)
    print(password_list)
    pass_index += 1


def run():
    # Initializing variables
    pass_length = 0
    done = False
    option = 0
    password_list = ['']
    password = ''
    pass_index = 0

    # Welcome and instructions:
    print('P A S S W O R D   G E N E R A T O R')

    while done == False:
        option = int(raw_input(
            '''
            Choose an option

            [1] Create a new password
            [2] View stored passwords
            [3] Delete a password
            [4] Change a current password
            [5] EXIT
            
            '''))

        if option == 5:
            done = True
        elif option == 1:
            generate_new_pass(password, password_list, pass_index)
        else:
            print('\nChoose a valid option!')            

    else:
        print('\nGOOD BYE!')


if __name__ == '__main__':
    run()