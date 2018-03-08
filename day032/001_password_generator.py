# -*- coding: utf-8 -*-
# Importing libraries
from __future__ import print_function
import random

def generate_new_pass(new_password, password_list, password_reference, pass_index):
    password_reference.append(str(raw_input('What\'s your password reference?: ')))
    pass_length = int(raw_input('Choose the character length of your password: ')) #Defines password strength
    # Generates random characters for the new password
    for i in range(0, pass_length):
        new_password.append(chr(random.randrange(32,126)))
        
    # Stores the password in a list
    password = ''.join(new_password)
    password_list.append(password)

    # Data output
    print('Password #{}: {} \nReference: {} '.format(pass_index + 1, password_list[pass_index], password_reference[pass_index]))

    # Clearing the list used to create the password
    for i in range(0, pass_length):
        new_password.pop()

def view_stored_passwords(pass_index, password_list, password_reference):
    for i in range(0, pass_index):
        print('Password #{}: {}'.format(i + 1, password_list[i]))
        print('Reference: {}\n'.format(password_reference[i]))

def run():
    # Initializing variables
    pass_length = 0
    done = False
    option = 0
    new_password = []
    password_reference = []
    password_list = []
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
            generate_new_pass(new_password, password_list, password_reference, pass_index)
            pass_index += 1
        elif option == 2:
            view_stored_passwords(pass_index, password_list, password_reference)
        else:
            print('\nChoose a valid option!')            

    else:
        print('\nGOOD BYE!')


if __name__ == '__main__':
    run()